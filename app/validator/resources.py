from flask_restful import request, Resource
from flask_jwt_extended import jwt_required

class ValidatorResource(Resource):

    @jwt_required
    def get(self):
        return True, 200