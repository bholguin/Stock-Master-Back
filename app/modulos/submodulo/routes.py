from app.modulos.submodulo.resources import SubmodulosResource
from flask import Blueprint
from flask_restful import Api

modulo_submodulos = Blueprint("modulo_submodulos", __name__)
api = Api(modulo_submodulos)

api.add_resource(SubmodulosResource, '/api/submodulos/', endpoint='submodulos')