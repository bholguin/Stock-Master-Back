from flask_restful import request, Resource
from flask_jwt_extended import jwt_required
from app.productos.schemas import ProductoSchema
from app.productos.models import Producto

producto_schema = ProductoSchema()

class ProductosResource(Resource):

    @jwt_required
    def get(self):
        productos = Producto.get_all()
        return producto_schema.dump(productos, many=True)
