def get_auth_headers(client):
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "test@example.com", "password": "test1234"},
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_job(client):
    headers = get_auth_headers(client)

    response = client.post(
        "/api/v1/jobs",
        json={"company": "Google", "role": "SWE", "status": "APPLIED"},
        headers=headers,
    )

    assert response.status_code == 201
    assert response.json()["company"] == "Google"


def test_list_job(client):
    headers = get_auth_headers(client)
    response = client.get("/api/v1/jobs", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def create_job_and_get_id(client, headers):
    response = client.post(
        "/api/v1/jobs/",
        json={"company": "Google", "role": "SWE", "status": "APPLIED"},
        headers=headers,
    )
    return response.json()["id"]


def test_get_job_by_id(client):
    headers = get_auth_headers(client)
    job_id = create_job_and_get_id(client, headers)

    response = client.get(f"/api/v1/jobs/{job_id}", headers=headers)

    assert response.status_code == 200
    assert response.json()["id"] == job_id


def test_update_job(client):
    headers = get_auth_headers(client)
    job_id = create_job_and_get_id(client, headers)

    response = client.put(
        f"/api/v1/jobs/{job_id}", json={"status": "INTERVIEW"}, headers=headers
    )

    assert response.status_code == 200
    assert response.json()["status"] == "INTERVIEW"


def test_delete_job(client):
    headers = get_auth_headers(client)
    job_id = create_job_and_get_id(client, headers)

    response = client.delete(f"/api/v1/jobs/{job_id}", headers=headers)

    assert response.status_code == 204

    response = client.get(f"/api/v1/jobs/{job_id}", headers=headers)

    assert response.status_code == 404


def get_auth_headers_utils(client, email, password):
    response = client.post(
        "/api/v1/auth/login", data={"username": email, "password": password}
    )
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_user_cannot_access_other_users_job(client):
    # user 1
    client.post(
        "/api/v1/auth/register",
        json={"email": "user1@test.com", "password": "pass1234"},
    )

    headers1 = get_auth_headers_utils(client, "user1@test.com", "pass1234")
    job_id = create_job_and_get_id(client, headers1)

    # user 2
    client.post(
        "/api/v1/auth/register",
        json={"email": "user2@test.com", "password": "pass1234"},
    )

    headers2 = get_auth_headers_utils(client, "user2@test.com", "pass1234")

    response = client.get(f"/api/v1/jobs/{job_id}", headers=headers2)

    assert response.status_code == 404
