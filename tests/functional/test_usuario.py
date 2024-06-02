

def test_usuario_module(custom_headers, client):

    response = client.get(
        "/api/usuarios", 
        headers=custom_headers,
    )

    users = response.get_json()

    assert len(users) > 0

    req = dict()
    req["nombre"] = "Juan"
    req["apellido"] = "Perez"
    req["correo"] = "juan@test.com"
    req["username"] = "jperez"
    req["identificacion"] = ""
    req["telefono"] = ""

    response = client.post(
        "/api/usuario", 
        headers=custom_headers,
        json=req
    )

    assert response.status == "201 CREATED"
    
    usr = response.get_json()

    response = client.delete(
        "/api/usuario", 
        headers=custom_headers,
        query_string={"id": usr["id"]},
    )

    assert response.status == "200 OK"