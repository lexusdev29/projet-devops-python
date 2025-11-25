from app import create_app

def test_home_status_code():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_api_hello():
    app = create_app()
    client = app.test_client()
    response = client.get("/api/hello")
    data = response.get_json()
    assert response.status_code == 200
    assert data["message"] == "Hello from the API!"

