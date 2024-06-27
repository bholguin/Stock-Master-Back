from flask_restful import request, Resource
from app.bodegas.model import Bodega
from app.bodegas.schemas import BodegasSchema
from flask_jwt_extended import jwt_required, get_current_user
from app.common.ext import oidc

bodega_schema = BodegasSchema()

class BodegasResource(Resource):

    @oidc.require_login
    def get(self):
        user = get_current_user()
        bodegas = Bodega.simple_filter(empresa_id=user.empresa_id)
        return bodega_schema.dump(bodegas, many=True), 200
    
class BodegaResource(Resource):

    @oidc.require_login
    def get(self):
        bodega_id = request.args['bodega_id']
        user = get_current_user()
        bodega = Bodega.get_bodega(bodega_id, user.empresa_id)
        return bodega_schema.dump(bodega), 200

    @oidc.require_login
    def post(self):
        user = get_current_user()
        bodega = Bodega.create_bodega(request.get_json(), user.empresa_id)
        return bodega_schema.dump(bodega), 201
    
    @oidc.require_login
    def put(self):
        user = get_current_user()
        bodega = Bodega.update_bodega(request.get_json(), user.empresa_id)
        return bodega_schema.dump(bodega), 200
    
    @oidc.require_login
    def delete(self):
        bodega_id = request.args['bodega_id']
        user = get_current_user()
        result = Bodega.delete_bodega(bodega_id, user.empresa_id)
        return result, 200
