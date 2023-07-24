from flask_restful import request, Resource
from app.vehiculos.models import Vehiculo
from app.vehiculos.schemas import VehiculoSchema
from flask_jwt_extended import jwt_required, get_current_user

vehiculo_schema = VehiculoSchema()


class VehiculosResource(Resource):

    @jwt_required
    def get(self):
        user = get_current_user()
        vehiculos = Vehiculo.simple_filter(empresa_id=user.empresa_id)
        return vehiculo_schema.dump(vehiculos, many=True)


class VehiculoResource(Resource):

    @jwt_required
    def get(self):
        vehiculo_id = request.args['vehiculo_id']
        user = get_current_user()
        vehiculo = Vehiculo.get_vehiculo(vehiculo_id, user.empresa_id)
        return vehiculo_schema.dump(vehiculo), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        vehi = Vehiculo.create_vehiculo(request.get_json(), empresa_id=user.empresa_id)
        return vehiculo_schema.dump(vehi), 201
    
    @jwt_required
    def put(self):
        vehiculo = Vehiculo.update_vehiculo(request.get_json())
        return vehiculo_schema.dump(vehiculo), 200
    
    @jwt_required
    def delete(self):
        vehiculo_id = request.args['vehiculo_id']
        user = get_current_user()
        result = Vehiculo.delete_vehiculo(vehiculo_id, user.empresa_id)
        return result, 200
