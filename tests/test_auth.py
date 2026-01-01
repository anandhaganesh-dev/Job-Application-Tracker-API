def test_user_registration(client):
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "test@example.com", "password": "test1234"},
    )
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"


def test_user_login(client):
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "test1234"},
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
