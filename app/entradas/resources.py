from flask_restful import Resource, request
from app.entradas.models import Entrada
from app.documentos.schemas import DocumentoSchema
from app.documentos.items.schemas import ItemSchema
from flask_jwt_extended import jwt_required, get_current_user

documentos_schema = DocumentoSchema()
items_schema = ItemSchema()

class EntradasResource(Resource):
    @jwt_required
    def get(self):
        user = get_current_user()
        entradas = Entrada.get_entradas(user.empresa_id)
        return documentos_schema.dump(entradas, many=True), 200

class EntradaResource(Resource):

    @jwt_required
    def get(self):
        entrada_id = request.args['entrada_id']
        user = get_current_user()
        entrada = Entrada.get_entrada(entrada_id, user.empresa_id)
        return documentos_schema.dump(entrada), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        entrada = Entrada.create_entrada(request.get_json(), user.id, user.empresa_id)
        return documentos_schema.dump(entrada), 201



class EntradaItemsResource(Resource):
    @jwt_required
    def get(self):
        entrada_id = request.args['entrada_id']
        items = Entrada.get_items(entrada_id)
        return items_schema.dump(items, many=True), 200


