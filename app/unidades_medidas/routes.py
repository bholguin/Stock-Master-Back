from app.unidades_medidas.resources import UnidadesMedidasResource
from flask import Blueprint
from flask_restful import Api

modulo_unidades_medidas = Blueprint('modulo_unidades_medidas', __name__)
api = Api(modulo_unidades_medidas)

api.add_resource(UnidadesMedidasResource, "/api/unidades_medidas", endpoint="empresa")