from app.movimientos.resources import KardexResource
from flask import Blueprint
from flask_restful import Api

modulo_movimientos = Blueprint("modulo_movimientos", __name__)
api = Api(modulo_movimientos)


api.add_resource(KardexResource, "/api/kardex/", endpoint="kardex")