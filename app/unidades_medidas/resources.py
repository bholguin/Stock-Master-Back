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
        unidad = UnidadesMedidas.get_by_id(unidad_id)
        return unidades_schema.dump(unidad), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        unidad = UnidadesMedidas.create_unidad(request.get_json(), empresa_id=user.empresa_id)
        return unidades_schema.dump(unidad), 201
    
    @jwt_required
    def put(self):
        unidad = UnidadesMedidas.update_unidad(request.get_json())
        return unidades_schema.dump(unidad), 200
    
    @jwt_required
    def delete(self):
        unidad_id = request.args['unidad_id']
        result = UnidadesMedidas.delete_unidad(unidad_id)
        return result, 200
