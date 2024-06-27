from flask_restful import request, Resource
from app.unidades_medidas.models import UnidadesMedidas
from app.unidades_medidas.schemas import UnidadesMedidasSchema
from flask_jwt_extended import jwt_required, get_current_user
from app.common.ext import oidc

unidades_schema = UnidadesMedidasSchema()

class UnidadesMedidasResource(Resource):

    @oidc.require_login
    def get(self):
        user = get_current_user()
        unidades = UnidadesMedidas.simple_filter(empresa_id=user.empresa_id)
        return unidades_schema.dump(unidades, many=True), 200
    
class UnidadMedidaResource(Resource):

    @oidc.require_login
    def get(self):
        unidad_id = request.args['unidad_id']
        user = get_current_user()
        unidad = UnidadesMedidas.get_unidad(unidad_id, user.empresa_id)
        return unidades_schema.dump(unidad), 200

    @oidc.require_login
    def post(self):
        user = get_current_user()
        unidad = UnidadesMedidas.create_unidad(request.get_json(), empresa_id=user.empresa_id)
        return unidades_schema.dump(unidad), 201
    
    @oidc.require_login
    def put(self):
        user = get_current_user()
        unidad = UnidadesMedidas.update_unidad(request.get_json(), user.empresa_id)
        return unidades_schema.dump(unidad), 200
    
    @oidc.require_login
    def delete(self):
        unidad_id = request.args['unidad_id']
        user = get_current_user()
        result = UnidadesMedidas.delete_unidad(unidad_id, user.empresa_id)
        return result, 200
