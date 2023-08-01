from flask_restful import Resource, request
from app.salidas.models import Salida
from app.documentos.schemas import DocumentoSchema
from app.documentos.items.schemas import ItemSchema
from flask_jwt_extended import jwt_required, get_current_user

documentos_schema = DocumentoSchema()
items_schema = ItemSchema()

class SalidasResource(Resource):
    @jwt_required
    def get(self):
        user = get_current_user()
        salidas = Salida.get_salidas(user.empresa_id)
        return documentos_schema.dump(salidas, many=True), 200

class SalidaResource(Resource):

    @jwt_required
    def get(self):
        salida_id = request.args['salida_id']
        user = get_current_user()
        salida = Salida.get_salida(salida_id, user.empresa_id)
        return documentos_schema.dump(salida), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        salida = Salida.create_salida(request.get_json(), user.id, user.empresa_id)
        return documentos_schema.dump(salida), 201



class SalidaItemsResource(Resource):
    @jwt_required
    def get(self):
        salida_id = request.args['salida_id']
        items = Salida.get_items(salida_id)
        return items_schema.dump(items, many=True), 200


