"""Pruebas del carrito y consistencia de cantidades."""

import pytest

from conftest import BASE_URL, TIMEOUT


@pytest.mark.lectura
def test_c01_consultar_carrito_existente(api):
    response = api.get(f"{BASE_URL}/carts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    cart = response.json()
    assert cart["id"] == 1
    assert isinstance(cart["products"], list) and cart["products"]
    assert isinstance(cart["userId"], int)


@pytest.mark.lectura
def test_c02_consistencia_cantidades(api):
    response = api.get(f"{BASE_URL}/carts/1", timeout=TIMEOUT)
    assert response.status_code == 200
    cart = response.json()
    assert cart["totalProducts"] == len(cart["products"])
    assert cart["totalQuantity"] == sum(p["quantity"] for p in cart["products"])
    assert all(p["quantity"] > 0 for p in cart["products"])


@pytest.mark.lectura
def test_c03_carritos_de_usuario(api):
    response = api.get(f"{BASE_URL}/carts/user/5", timeout=TIMEOUT)
    assert response.status_code == 200
    carts = response.json()["carts"]
    assert isinstance(carts, list)
    assert all(cart["userId"] == 5 for cart in carts)


@pytest.mark.escritura
def test_c04_agregar_carrito_simulado(api):
    payload = {"userId": 1, "products": [{"id": 1, "quantity": 2}]}
    response = api.post(f"{BASE_URL}/carts/add", json=payload, timeout=TIMEOUT)
    assert response.status_code in (200, 201)
    cart = response.json()
    assert cart["userId"] == 1
    assert cart["totalQuantity"] == 2
