from app.common.ext import mh
from app.movimientos.models import Movimiento


class MovimientoSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Movimiento

    id = mh.auto_field(dump_only=True)
    documento = mh.Nested('DocumentoSchema')