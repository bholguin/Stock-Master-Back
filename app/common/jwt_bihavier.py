from flask import jsonify
from app.validator.models import TokenBlacklist
from app.usuarios.models import Usuario


def jwt_callbacks(jwt):

    @jwt.token_in_blacklist_loader
    def check_if_token_in_blacklist(decrypted_token):
        return TokenBlacklist.valida_jti_blacklist(decrypted_token['jti'])

    @jwt.expired_token_loader
    def expired_token(expired_token):
        return TokenBlacklist.expired_token_app(expired_token['jti'])

    @jwt.user_identity_loader
    def user_identity_lookup(user):
        return user.id

    @jwt.user_loader_callback_loader
    def user_lookup_callback(id):
        try:
            return Usuario.query.filter_by(id=id).one_or_none()
        except:
            print('without identity')
