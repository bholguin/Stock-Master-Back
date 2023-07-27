from flask_restful import Resource
from app.modulos.submodulo.models import Submodulo
from app.modulos.submodulo.schemas import SubmoduloSchema
from flask_jwt_extended import jwt_required

submodulo_schema = SubmoduloSchema()
class SubmodulosDocumentoResource(Resource):
    @jwt_required
    def get(self):
        submodulos = Submodulo.simple_filter(tipo_doc=True)
        return submodulo_schema.dump(submodulos, many=True), 200

class SubmodulosResource(Resource):
    pass




