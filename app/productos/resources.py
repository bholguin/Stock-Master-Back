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
    def get(self):
        unidad_id = request.args['producto_id']
        user = get_current_user()
        unidad = Producto.get_producto(unidad_id, user.empresa_id)
        return producto_schema.dump(unidad), 200

    @jwt_required
    def post(self):
        user = get_current_user()
        producto = Producto.create_producto(request.get_json(), empresa_id=user.empresa_id)
        return producto_schema.dump(producto), 201
    
    @jwt_required
    def put(self):
        producto = Producto.update_producto(request.get_json())
        return producto_schema.dump(producto), 200

    @jwt_required
    def delete(self):
        producto_id = request.args['producto_id']
        user = get_current_user()
        result = Producto.delete_producto(producto_id, user.empresa_id)
        return result, 200
