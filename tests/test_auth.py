"""Autenticación con credenciales de DEMOSTRACIÓN publicadas por DummyJSON."""

import pytest

from conftest import BASE_URL, TIMEOUT


@pytest.mark.auth
def test_a01_login_valido(api):
    response = api.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys", "password": "emilyspass"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    assert response.json()["username"] == "emilys"
    assert isinstance(response.json()["accessToken"], str)


@pytest.mark.auth
def test_a02_login_invalido(api):
    response = api.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys", "password": "incorrecta-qa"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 400
    assert response.json().get("message")


@pytest.mark.auth
def test_a03_usuario_autenticado(api, demo_token):
    response = api.get(
        f"{BASE_URL}/auth/me",
        headers={"Authorization": f"Bearer {demo_token}"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    assert response.json()["username"] == "emilys"
