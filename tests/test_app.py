from app import create_app


def test_home():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_api():
    app = create_app()
    client = app.test_client()
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hello from the API!"
