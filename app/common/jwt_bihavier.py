from flask import jsonify
from app.validator.models import TokenBlacklist


def jwt_callbacks(jwt):

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return TokenBlacklist.valida_jti_blacklist(decrypted_token['jti'])

    @jwt.expired_token_loader
    def expired_token(expired_token):
        return TokenBlacklist.expired_token_app(expired_token['jti'])
        
