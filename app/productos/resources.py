from flask_restful import request, Resource
from flask_jwt_extended import jwt_required, get_current_user
from app.productos.schemas import ProductoSchema
from app.productos.models import Producto

producto_schema = ProductoSchema()

class ProductosResource(Resource):

    @jwt_required
    def get(self):
        productos = Producto.get_all()
        return producto_schema.dump(productos, many=True)
    
class ProductoResource(Resource):

    @jwt_required
    def post(self):
        user = get_current_user()
        producto = Producto.create_producto(request.get_json(), empresa_id=user.empresa_id)
        return producto_schema.dump(producto), 201
