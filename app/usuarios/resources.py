from flask_restful import request, Resource
from .models import Usuario
from .schemas import UsuarioSchema
from flask_jwt_extended import jwt_required, current_user, get_current_user

usuario_schema = UsuarioSchema()

class ChangePasswordResource(Resource):

    @jwt_required
    def put(self):
        user = get_current_user()
        return Usuario.update_password(request.get_json(), user.id)

class UsuariosResource(Resource):

    @jwt_required
    def get(self):
        usuarios = Usuario.get_all()
        return usuario_schema.dump(usuarios, many=True)

class UsuarioResource(Resource):

    @jwt_required
    def get(self):
        return usuario_schema.dump(current_user)

    @jwt_required
    def post(self):
        user = Usuario.create_user(request.get_json())
        return usuario_schema.dump(user) , 201

    @jwt_required
    def delete(self, id):
        Usuario.delete_user(id)
        return id, 200

    @jwt_required
    def put(self):
        user = Usuario.update_user(request.get_json())
        return usuario_schema.dump(user), 201


