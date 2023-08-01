from app.salidas.resources import SalidasResource, SalidaResource, SalidaItemsResource
from flask import Blueprint
from flask_restful import Api

modulo_salidas = Blueprint("modulo_salidas", __name__)
api = Api(modulo_salidas)


api.add_resource(SalidaResource, "/api/salida/", endpoint="salida")
api.add_resource(SalidasResource, "/api/salidas/", endpoint="salidas")
api.add_resource(SalidaItemsResource, "/api/salida-items", endpoint="salida-items")