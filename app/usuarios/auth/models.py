from app.common.error_handling import LoginNotFound, EmptyMessage
from app.usuarios.models import Usuario
from app.validator.models import TokenBlacklist


class Login():

    token: str

    def __init__(self, token):
        self.token = token

    @classmethod
    def logout_method(self, jti: str):
        token = TokenBlacklist.filter_first(jti=jti)
        token.revoked = True
        token.update()
        raise EmptyMessage
    
    @classmethod
    def login_method(self, data: dict):
        try:
            username = data['username']
            password = data['password']
        except:
            raise LoginNotFound()
        user = Usuario.filter_first(username=username)
        if user and user.check_password(user.password, password):
            auth_token = TokenBlacklist.encode_auth_token_extended(user)
            return auth_token
        else:
            raise LoginNotFound()