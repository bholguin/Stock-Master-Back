from flask_restful import request, Resource
from app.vehiculos.models import Vehiculo
from app.vehiculos.schemas import VehiculoSchema
from app.common.ext import oidc
from flask_jwt_extended import jwt_required, get_current_user

vehiculo_schema = VehiculoSchema()


class VehiculosResource(Resource):

    @oidc.require_login
    def get(self):
        user = get_current_user()
        vehiculos = Vehiculo.simple_filter(empresa_id=user.empresa_id)
        return vehiculo_schema.dump(vehiculos, many=True)


class VehiculoResource(Resource):

    @oidc.require_login
    def get(self):
        vehiculo_id = request.args['vehiculo_id']
        user = get_current_user()
        vehiculo = Vehiculo.get_vehiculo(vehiculo_id, user.empresa_id)
        return vehiculo_schema.dump(vehiculo), 200

    @oidc.require_login
    def post(self):
        user = get_current_user()
        vehi = Vehiculo.create_vehiculo(request.get_json(), empresa_id=user.empresa_id)
        return vehiculo_schema.dump(vehi), 201
    
    @oidc.require_login
    def put(self):
        user = get_current_user()
        vehiculo = Vehiculo.update_vehiculo(request.get_json(), user.empresa_id)
        return vehiculo_schema.dump(vehiculo), 200
    
    @oidc.require_login
    def delete(self):
        vehiculo_id = request.args['vehiculo_id']
        user = get_current_user()
        result = Vehiculo.delete_vehiculo(vehiculo_id, user.empresa_id)
        return result, 200
