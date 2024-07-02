from fastapi import status
from fastapi.testclient import TestClient

from fast_zero_2025.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'Olá Mundo!'}
