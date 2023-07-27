from flask_restful import request, Resource
from app.tipos_documento.models import TipoDocumento
from app.tipos_documento.schemas import TipoDocumentoSchema
from flask_jwt_extended import jwt_required, get_current_user

tipodoc_schema = TipoDocumentoSchema()

class TiposDocumentoResource(Resource):

    @jwt_required
    def get(self):
        user = get_current_user()
        tipos_doc = TipoDocumento.simple_filter(empresa_id=user.empresa_id)
        return tipodoc_schema.dump(tipos_doc, many=True), 200
    
class TipoDocumentoResource(Resource):

    @jwt_required
    def get(self):
        tipodoc_id = request.args['tipodoc_id']
        user = get_current_user()
        tipodoc = TipoDocumento.get_tipo_doc(tipodoc_id, user.empresa_id)
        return tipodoc_schema.dump(tipodoc), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        tipodoc = TipoDocumento.create_tipodoc(request.get_json(), empresa_id=user.empresa_id)
        return tipodoc_schema.dump(tipodoc), 201
    
    @jwt_required
    def put(self):
        user = get_current_user()
        tipodoc = TipoDocumento.update_tipodoc(request.get_json(), user.empresa_id)
        return tipodoc_schema.dump(tipodoc), 200

