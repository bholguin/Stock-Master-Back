from app.common.ext import mh 
from app.vehiculos.models import Vehiculo


class VehiculoSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Vehiculo
    
    id = mh.auto_field(dump_only=True)