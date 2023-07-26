from flask_restful import request, Resource
from app.unidades_medidas.models import UnidadesMedidas
from app.unidades_medidas.schemas import UnidadesMedidasSchema
from flask_jwt_extended import jwt_required, get_current_user

unidades_schema = UnidadesMedidasSchema()

class UnidadesMedidasResource(Resource):

    @jwt_required
    def get(self):
        user = get_current_user()
        unidades = UnidadesMedidas.simple_filter(empresa_id=user.empresa_id)
        return unidades_schema.dump(unidades, many=True), 200
    
class UnidadMedidaResource(Resource):

    @jwt_required
    def get(self):
        unidad_id = request.args['unidad_id']
        user = get_current_user()
        unidad = UnidadesMedidas.get_unidad(unidad_id, user.empresa_id)
        return unidades_schema.dump(unidad), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        unidad = UnidadesMedidas.create_unidad(request.get_json(), empresa_id=user.empresa_id)
        return unidades_schema.dump(unidad), 201
    
    @jwt_required
    def put(self):
        user = get_current_user()
        unidad = UnidadesMedidas.update_unidad(request.get_json(), user.empresa_id)
        return unidades_schema.dump(unidad), 200
    
    @jwt_required
    def delete(self):
        unidad_id = request.args['unidad_id']
        user = get_current_user()
        result = UnidadesMedidas.delete_unidad(unidad_id, user.empresa_id)
        return result, 200
