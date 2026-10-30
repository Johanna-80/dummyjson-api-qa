"""Validaciones de catálogo, búsqueda, filtros y CRUD simulado."""

import pytest

from conftest import BASE_URL, TIMEOUT


@pytest.mark.lectura
def test_p01_listar_productos_devuelve_estructura(api):
    response = api.get(f"{BASE_URL}/products", timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data["products"], list) and data["products"]
    assert isinstance(data["total"], int) and data["total"] > 0
    assert all({"id", "title", "price", "category"} <= set(item) for item in data["products"])


@pytest.mark.lectura
def test_p02_producto_existente_por_id(api):
    response = api.get(f"{BASE_URL}/products/1", timeout=TIMEOUT)
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert isinstance(product["title"], str) and product["title"]
    assert product["price"] >= 0


@pytest.mark.lectura
def test_p03_producto_inexistente_devuelve_404(api):
    response = api.get(f"{BASE_URL}/products/99999999", timeout=TIMEOUT)
    assert response.status_code == 404
    assert "message" in response.json()


@pytest.mark.lectura
def test_p04_busqueda_por_texto(api):
    response = api.get(f"{BASE_URL}/products/search", params={"q": "phone"}, timeout=TIMEOUT)
    assert response.status_code == 200
    products = response.json()["products"]
    assert products and all("phone" in p["title"].lower() or "phone" in p.get("description", "").lower() for p in products)


@pytest.mark.lectura
def test_p05_busqueda_sin_coincidencias(api):
    response = api.get(f"{BASE_URL}/products/search", params={"q": "zzzxxyy-no-existe-987"}, timeout=TIMEOUT)
    assert response.status_code == 200
    assert response.json()["products"] == []
    assert response.json()["total"] == 0


@pytest.mark.lectura
def test_p06_paginacion_limite_y_desplazamiento(api):
    response = api.get(f"{BASE_URL}/products", params={"limit": 5, "skip": 10}, timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert len(data["products"]) == 5
    assert data["skip"] == 10
    assert data["limit"] == 5


@pytest.mark.lectura
def test_p07_filtrar_categoria(api):
    response = api.get(f"{BASE_URL}/products/category/smartphones", timeout=TIMEOUT)
    assert response.status_code == 200
    products = response.json()["products"]
    assert products and all(p["category"] == "smartphones" for p in products)


@pytest.mark.lectura
def test_p08_orden_ascendente_por_precio(api):
    response = api.get(f"{BASE_URL}/products", params={"sortBy": "price", "order": "asc", "limit": 20}, timeout=TIMEOUT)
    assert response.status_code == 200
    prices = [product["price"] for product in response.json()["products"]]
    assert prices == sorted(prices)


@pytest.mark.lectura
def test_p09_proyeccion_de_campos(api):
    response = api.get(f"{BASE_URL}/products", params={"limit": 3, "select": "title,price"}, timeout=TIMEOUT)
    assert response.status_code == 200
    products = response.json()["products"]
    assert len(products) == 3
    assert all({"title", "price"} <= set(p) for p in products)


@pytest.mark.escritura
def test_p10_creacion_simulada_de_producto(api):
    response = api.post(f"{BASE_URL}/products/add", json={"title": "Producto QA de prueba", "price": 29.99}, timeout=TIMEOUT)
    assert response.status_code in (200, 201)
    body = response.json()
    assert body["title"] == "Producto QA de prueba"
    assert body["price"] == 29.99
    assert isinstance(body["id"], int)


@pytest.mark.escritura
def test_p11_actualizacion_simulada_de_producto(api):
    response = api.put(f"{BASE_URL}/products/1", json={"title": "Título actualizado QA"}, timeout=TIMEOUT)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["title"] == "Título actualizado QA"


@pytest.mark.escritura
def test_p12_eliminacion_simulada_de_producto(api):
    response = api.delete(f"{BASE_URL}/products/1", timeout=TIMEOUT)
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["isDeleted"] is True
