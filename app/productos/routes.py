from app.productos.resources import ProductosResource
from flask import Blueprint
from flask_restful import Api

modulo_producto = Blueprint("modulo_producto", __name__)
api = Api(modulo_producto)


api.add_resource(ProductosResource, "/api/productos/", endpoint="productos")