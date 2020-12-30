from flask import Blueprint
from flask_restful import Api

modulo_token = Blueprint('modulo_token', __name__)
api = Api(modulo_token)
