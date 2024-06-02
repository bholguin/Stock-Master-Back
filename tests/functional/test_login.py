def test_login(client):
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

    assert response.status == "200 OK"
    assert isinstance(json_response, str)

    

def test_login_unexisting_tenant(client):
    req = dict()
    req["username"] = "admin"
    req["password"] = "1234"
    req["empresa_id"] = 0

    response = client.post(
        "/api/login", 
        headers={"Content-Type": "application/json"},
        json=req
    )

    assert response.status == "404 NOT FOUND"