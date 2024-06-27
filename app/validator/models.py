from flask import jsonify
from app.common.db import db, BaseModel
from app.common.error_handling import ForbiddenError
from datetime import datetime
from flask_jwt_extended import (
    create_access_token, decode_token
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, DateTime

class TokenBlacklist(db.Model, BaseModel):
    __tablename__ = 'token_blacklist'
    id: Mapped[int] = mapped_column(primary_key=True)
    jti: Mapped[str] = mapped_column(String(36))
    token_type: Mapped[str] = mapped_column(String(10))
    user_identity: Mapped[str] = mapped_column(String(50))
    revoked: Mapped[bool] = mapped_column(Boolean)
    expires = mapped_column(DateTime)

    def __init__(self, jti, token_type, user_identity, revoked, expires):
        self.jti = jti
        self.token_type = token_type
        self.user_identity = user_identity
        self.revoked = revoked
        self.expires = expires

    # como claims se puede pasar el listado de permisos por el token
    @classmethod
    def encode_auth_token_extended(self, user):
        access_token = create_access_token(identity=user)
        decode_token = self.decode_auth_token_extended(access_token)
        bl = TokenBlacklist(
            jti=decode_token['jti'],
            token_type=decode_token['type'],
            user_identity=decode_token['identity'],
            revoked=False,
            expires=datetime.fromtimestamp(decode_token['exp'])
        )
        bl.save()
        return access_token

    @classmethod
    def expired_token_app(self, jti):
        token = self.filter_first(jti=jti)
        token.revoked = True
        token.update()
        if token.revoked:
            return jsonify({
                'status': 401,
                'sub_status': 42,
                'msg': 'The token has expired'
            }), 401
        return jsonify({
            'status': 200,
            'msg': 'Active'
        }), 200

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
