from flask_restful import request, Resource
from app.tipos_documento.models import TipoDocumento
from app.tipos_documento.schemas import TipoDocumentoSchema
from flask_jwt_extended import jwt_required, get_current_user
from app.common.ext import oidc

tipodoc_schema = TipoDocumentoSchema()

class TiposDocumentoResource(Resource):

    @oidc.require_login
    def get(self):
        submodulo_id = request.args.get('submodulo_id', None)
        user = get_current_user()
        if submodulo_id is None:
            tipos_doc = TipoDocumento.simple_filter(empresa_id=user.empresa_id)
            return tipodoc_schema.dump(tipos_doc, many=True), 200
        else:
            tipos_doc = TipoDocumento.simple_filter(empresa_id=user.empresa_id, submodulo_id=submodulo_id)
            return tipodoc_schema.dump(tipos_doc, many=True), 200

    
class TipoDocumentoResource(Resource):

    @oidc.require_login
    def get(self):
        tipodoc_id = request.args['tipodoc_id']
        user = get_current_user()
        tipodoc = TipoDocumento.get_tipo_doc(tipodoc_id, user.empresa_id)
        return tipodoc_schema.dump(tipodoc), 200

    @oidc.require_login
    def post(self):
        user = get_current_user()
        tipodoc = TipoDocumento.create_tipodoc(request.get_json(), empresa_id=user.empresa_id)
        return tipodoc_schema.dump(tipodoc), 201
    
    @oidc.require_login
    def put(self):
        user = get_current_user()
        tipodoc = TipoDocumento.update_tipodoc(request.get_json(), user.empresa_id)
        return tipodoc_schema.dump(tipodoc), 200

    @oidc.require_login
    def delete(self):
        tipodoc_id = request.args['tipodoc_id']
        user = get_current_user()
        result = TipoDocumento.delete_tipodoc(tipodoc_id, user.empresa_id)
        return result, 200
