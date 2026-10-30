"""Fixtures compartidos para las pruebas de DummyJSON.

Los usuarios de demostración son públicos y están documentados por DummyJSON.
No se almacenan tokens de sesión en archivos ni en el repositorio.
"""

import os

import pytest
import requests


BASE_URL = os.getenv("DUMMYJSON_BASE_URL", "https://dummyjson.com").rstrip("/")
TIMEOUT = 15


@pytest.fixture(scope="session")
def api():
    with requests.Session() as session:
        session.headers.update({"Accept": "application/json"})
        yield session


@pytest.fixture(scope="session")
def demo_token(api):
    response = api.post(
        f"{BASE_URL}/auth/login",
        json={"username": "emilys", "password": "emilyspass"},
        timeout=TIMEOUT,
    )
    assert response.status_code == 200, "El login de demostración debe funcionar"
    token = response.json().get("accessToken")
    assert isinstance(token, str) and token
    return token
