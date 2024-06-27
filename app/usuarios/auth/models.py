from app.common.error_handling import EmptyMessage, ForbiddenError, ObjectNotFound
from app.usuarios.models import Usuario
from app.empresas.models import Empresa
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
            empresa_id = data['empresa_id']
        except:
            raise ForbiddenError()

        empresa = Empresa.get_by_id(empresa_id)
        if(empresa == None):
            raise ObjectNotFound()
     
        user = Usuario.filter_first(username=username, empresa_id=empresa_id)
        if user and user.check_password(user.password, password):
            auth_token = TokenBlacklist.encode_auth_token_extended(user)
            return dict(token= auth_token, usuario = user, empresa = empresa)
        else:
            raise ForbiddenError()