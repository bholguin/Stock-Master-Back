from flask import jsonify
from app.validator.models import TokenBlacklist


def jwt_callbacks(jwt):

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return TokenBlacklist.valida_jti_blacklist(decrypted_token['jti'])


    @jwt.expired_token_loader
    def expired_token(expired_token):
        jti = expired_token['jti']
        token = TokenBlacklist.filter_first(jti=jti)
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
