from app.modulos.resources import ModulosResource, ModulosDocumentoResource
from flask import Blueprint
from flask_restful import Api

modulo_modulos = Blueprint("modulo_modulos", __name__)
api = Api(modulo_modulos)

api.add_resource(ModulosDocumentoResource, '/api/modulos-con-documentos', endpoint='modulos-documentos')
api.add_resource(ModulosResource, '/api/modulos/', endpoint='modulos')