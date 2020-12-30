from .resources import LoginResource, LogoutResource
from flask import Blueprint
from flask_restful import Api

modulo_login = Blueprint('modulo_login', __name__)
api = Api(modulo_login)

api.add_resource(LoginResource, '/api/login', endpoint='login')
api.add_resource(LogoutResource, '/api/logout', endpoint='logout')