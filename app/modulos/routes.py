from app.modulos.resources import ModulosResource
from flask import Blueprint
from flask_restful import Api

modulo_modulos = Blueprint("modulo_modulos", __name__)
api = Api(modulo_modulos)

api.add_resource(ModulosResource, '/api/modulos/', endpoint='modulos')