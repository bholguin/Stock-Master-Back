

def test_usuario_module(custom_headers, client) -> None:

    # CREATE USER
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
    # GET USER BY ID
    response = client.get(
        "/api/usuario", 
        headers=custom_headers,
         query_string={"usuario_id": usr["id"]},
    )

    usr = response.get_json()

    assert usr["username"] == "jperez"


    # UPDATE USER 
    usr["telefono"] = "123456789"

    response = client.put(
        "/api/usuario", 
        headers=custom_headers,
        json=usr
    )

    usr = response.get_json()

    assert response.status == "200 OK"
    assert usr["telefono"] == "123456789"

    # GET ALL USERS
    response = client.get(
        "/api/usuarios", 
        headers=custom_headers,
    )

    users = response.get_json()

    assert len(users) > 0

    # DELETE USER
    response = client.delete(
        "/api/usuario", 
        headers=custom_headers,
        query_string={"id": usr["id"]},
    )

    assert response.status == "200 OK"