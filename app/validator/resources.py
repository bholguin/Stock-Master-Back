from flask_restful import request, Resource
from app.vehiculos.models import Vehiculo
from flask_jwt_extended import jwt_required, get_jwt_identity

class ValidatorResource(Resource):

    @jwt_required
    def get(self):
        return True, 200