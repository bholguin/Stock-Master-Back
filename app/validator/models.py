from app.common.db import db, BaseModel
from app.common.error_handling import ForbiddenError
from datetime import datetime
from flask_jwt_extended import (
    create_access_token, decode_token
)


class TokenBlacklist(db.Model, BaseModel):
    __tablename__ = 'token_blacklist'
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False)
    token_type = db.Column(db.String(10), nullable=False)
    user_identity = db.Column(db.String(50), nullable=False)
    revoked = db.Column(db.Boolean, nullable=False)
    expires = db.Column(db.DateTime, nullable=False)

    def __init__(self, jti, token_type, user_identity, revoked, expires):
        self.jti = jti
        self.token_type = token_type
        self.user_identity = user_identity
        self.revoked = revoked
        self.expires = expires

    # como claims se puede pasar el listado de permisos por el token
    @classmethod
    def encode_auth_token_extended(self, id):
        access_token = create_access_token(identity=id)
        decode_token = self.decode_auth_token_extended(access_token)
        bl = TokenBlacklist(
            jti= decode_token['jti'],
            token_type= decode_token['type'],
            user_identity= decode_token['identity'],
            revoked= False,
            expires= datetime.fromtimestamp(decode_token['exp'])
        )
        bl.save()
        return access_token

    @classmethod
    def decode_auth_token_extended(self, token):
        return decode_token(token)

    @classmethod
    def valida_token_blacklist(self, token: str):
        return self.filter_first(token=token)

    @classmethod
    def valida_jti_blacklist(self, jti: str) -> bool:
        modelo = self.filter_first(jti=jti)
        if modelo:
            return modelo.revoked
        return True 
