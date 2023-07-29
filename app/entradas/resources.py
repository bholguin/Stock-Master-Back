from flask_restful import Resource
from app.entradas.models import Entrada
from app.documentos.schemas import DocumentoSchema
from flask_jwt_extended import jwt_required, get_current_user

documentos_schema = DocumentoSchema()

class EntradasResource(Resource):
    @jwt_required
    def get(self):
        user = get_current_user()
        entradas = Entrada.get_entradas(user.empresa_id)
        return documentos_schema.dump(entradas, many=True), 200






