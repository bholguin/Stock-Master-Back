from flask import jsonify, make_response
from flask_restful import request, Resource
from app.usuarios.auth.models import Login
from app.usuarios.auth.schemas import LoginSchema
from flask_jwt_extended import jwt_required, get_raw_jwt

login_schema = LoginSchema()

class LogoutResource(Resource):

    @jwt_required
    def put(self):
        return Login.logout_method(get_raw_jwt()['jti'])
        
class LoginResource(Resource):
    
    def post(self):
        values = Login.login_method(request.get_json())
        login = login_schema.dump(values)
        print(login)
        return  login, 200




