from app.vehiculos.resources import VehiculoResource, VehiculosResource
from flask import Blueprint
from flask_restful import Api


modulo_vehiculos = Blueprint("modulo_vehiculos", __name__)
api = Api(modulo_vehiculos)

api.add_resource(VehiculoResource, "/api/vehiculo/", endpoint="vehiculo")
api.add_resource(VehiculosResource, "/api/vehiculos/", endpoint="vehiculos")