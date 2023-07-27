from app.modulos.submodulo.resources import SubmodulosResource, SubmodulosDocumentoResource
from flask import Blueprint
from flask_restful import Api

modulo_submodulos = Blueprint("modulo_submodulos", __name__)
api = Api(modulo_submodulos)

api.add_resource(SubmodulosResource, '/api/submodulos/', endpoint='submodulos')
api.add_resource(SubmodulosDocumentoResource, '/api/submodulos-con-documentos', endpoint='submodulos-con-documentos')