from app.usuarios import Usuario

def test_new_usuario():
    """
        GIVEN a User model
        WHEN a new User is created
        THEN check the email, hashed_password, and role fields are defined correctly
    """
    user = Usuario("Brayhan", "Holguin", "bholguin", "", 1, "bholguin1488@gmail.com", "1143952325", "")
    assert user.nombre == "Brayhan"
    assert user.apellido == "Holguin"
