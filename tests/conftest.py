import pytest
from app import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def token(client):
    req = dict()
    req["username"] = "admin"
    req["password"] = "1234"
    req["empresa_id"] = 1

    response = client.post(
        "/api/login", 
        headers={"Content-Type": "application/json"},
        json=req
    )
    
    json_response = response.get_json()

    return "Bearer "+json_response


@pytest.fixture()
def custom_headers(token):
    return {
        "Content-Type": "application/json",
        "Authorization": token
    }