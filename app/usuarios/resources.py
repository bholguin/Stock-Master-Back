from flask_restful import request, Resource
from .models import Usuario
from .schemas import UsuarioSchema
from flask_jwt_extended import jwt_required, get_current_user

usuario_schema = UsuarioSchema()

class ChangePasswordResource(Resource):

    @jwt_required
    def put(self):
        user = get_current_user()
        return Usuario.update_password(request.get_json(), user.id)

class UsuariosResource(Resource):

    @jwt_required
    def get(self):
        user = get_current_user()
        usuarios = Usuario.get_users(user.id, user.empresa_id)
        return usuario_schema.dump(usuarios, many=True)

class UsuarioResource(Resource):

    @jwt_required
    def get(self):
        usuario_id = request.args.get('usuario_id', None)

        current_user = get_current_user()

        if usuario_id is None:
            return usuario_schema.dump(current_user)
        else:
            usuario = Usuario.get_user(usuario_id, current_user.empresa_id)
            return usuario_schema.dump(usuario)
        
    @jwt_required
    def post(self):
        current_user = get_current_user()
        user = Usuario.create_user(request.get_json(), current_user.empresa_id)
        return usuario_schema.dump(user) , 201

    @jwt_required
    def delete(self):
        current_user = get_current_user()
        id = request.args['id']
        Usuario.delete_user(id, current_user.empresa_id)
        return id, 200

    @jwt_required
    def put(self):
        current_user = get_current_user()
        user = Usuario.update_user(request.get_json(), current_user.empresa_id)
        return usuario_schema.dump(user), 201


