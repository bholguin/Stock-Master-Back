from flask_restful import Resource
from app.modulos.models import Modulo
from app.modulos.schemas import ModuloSchema
from flask_jwt_extended import jwt_required

modulo_schema = ModuloSchema()

class ModulosDocumentoResource(Resource):
    @jwt_required
    def get(self):
        modulos = Modulo.modulos_with_document()
        return modulo_schema.dump(modulos, many=True), 200

class ModulosResource(Resource):

    def get(self):
        return Modulo.get_all()




