from flask import jsonify
from flask_restful import request, Resource
from app.usuarios.auth.models import Login
from app.usuarios.auth.schemas import LoginSchema
from flask_jwt_extended import jwt_required, get_raw_jwt, set_access_cookies

login_schema = LoginSchema()

class LogoutResource(Resource):

    @jwt_required
    def get(self):
        return Login.logout_method(get_raw_jwt()['jti'])
        
class LoginResource(Resource):
    
    def post(self):
        token = Login.login_method(request.get_json())
        resp = jsonify({'refresh': True})
        set_access_cookies(resp, token)
        return  token, 200




