from app.entradas.resources import EntradasResource, EntradaResource, EntradaItemsResource
from flask import Blueprint
from flask_restful import Api

modulo_entradas = Blueprint("modulo_entradas", __name__)
api = Api(modulo_entradas)


api.add_resource(EntradasResource, "/api/entradas/", endpoint="entradas")
api.add_resource(EntradaResource, "/api/entrada/", endpoint="entrada")
api.add_resource(EntradaItemsResource, "/api/entrada-items", endpoint="entrada-items")