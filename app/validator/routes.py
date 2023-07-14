from app.validator.resources import ValidatorResource
from flask import Blueprint
from flask_restful import Api


modulo_validator = Blueprint("modulo_validator", __name__)
api = Api(modulo_validator)

api.add_resource(ValidatorResource, "/api/validator/", endpoint="validator")
