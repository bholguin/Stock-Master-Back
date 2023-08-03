from flask_restful import request, Resource
from flask_jwt_extended import jwt_required, get_current_user
from app.movimientos.schemas import MovimientoSchema
from app.movimientos.models import Movimiento

movimientos_schema = MovimientoSchema()

class KardexResource(Resource):
    @jwt_required
    def get(self):
        user = get_current_user()
        producto_id = request.args['producto_id']
        bodega_id = request.args['bodega_id']
        movimientos = Movimiento.get_kadex(user.empresa_id, producto_id, bodega_id)
        return movimientos_schema.dump(movimientos, many=True)