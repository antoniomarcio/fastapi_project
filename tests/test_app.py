from http import HTTPStatus


def test_read_root__retornar_ok_e_ola_mundo(client):  # Arrange (organização)
    response = client.get('/')  # Act (ação)

    assert response.status_code == HTTPStatus.OK  # Assert (afirmação)

    assert response.json() == {'message': 'Olá mundo!'}  # Assert (afirmação)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test',
            'password': 'testtest',
            'email': 'test@test.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
        'username': 'test',
        'email': 'test@test.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'username': 'test',
                'email': 'test@test.com',
                'id': 1,
            }
        ]
    }
