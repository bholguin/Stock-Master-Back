from flask_restful import request, Resource
from app.vehiculos.models import Vehiculo
from app.vehiculos.schemas import VehiculoSchema
from flask_jwt_extended import jwt_required

vehiculo_schema = VehiculoSchema()


class VehiculosResource(Resource):

    @jwt_required
    def get(self):
        vehiculos = Vehiculo.get_all()
        return vehiculo_schema.dump(vehiculos, many=True)


class VehiculoResource(Resource):

    @jwt_required
    def post(self):
        vehi = Vehiculo.create_vehiculo(request.get_json())
        return vehiculo_schema.dump(vehi), 201