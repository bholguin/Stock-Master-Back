from .resources import BodegaResource, BodegasResource
from flask import Blueprint
from flask_restful import Api

modulo_bodegas = Blueprint('modulo_bodegas', __name__)
api = Api(modulo_bodegas)

api.add_resource(BodegaResource, '/api/bodega/', endpoint='bodega')
api.add_resource(BodegasResource, '/api/bodegas/', endpoint='bodegas')
