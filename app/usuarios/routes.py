from flask import Blueprint
from flask_restful import Api
from app.usuarios.resources import UsuariosResource, UsuarioResource, ChangePasswordResource

modulo_usuarios = Blueprint('modulo_usuarios', __name__)
api = Api(modulo_usuarios)

api.add_resource(UsuarioResource, '/api/usuario/', endpoint='usuario')
api.add_resource(UsuariosResource, '/api/usuarios/', endpoint='usuarios')
api.add_resource(ChangePasswordResource, '/api/usuario/change-password' , endpoint='change-password')