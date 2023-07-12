from flask_restful import request, Resource
from app.unidades_medidas.models import UnidadesMedidas
from app.unidades_medidas.schemas import UnidadesMedidasSchema
from flask_jwt_extended import jwt_required

unidades_schema = UnidadesMedidasSchema()

class UnidadesMedidasResource(Resource):

    def get(self):
        unidades = UnidadesMedidas.get_all()
        return unidades_schema.dump(unidades, many=True), 200