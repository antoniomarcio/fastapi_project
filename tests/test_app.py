from http import HTTPStatus

import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app


@pytest.fixture
def client():
    return TestClient(app=app)


def test_read_root_deve_retornar_ok_e_ola_mundo(client):  # Arrange (organizar)
    response = client.get('/')  # Act (agir)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmar)

    assert response.json() == {'message': 'Olá mundo!'}  # Assert (afirmar)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_username',
            'password': 'test_password',
            'email': 'test@email.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'test_username',
        'email': 'test@email.com',
        'id': 1,
    }
