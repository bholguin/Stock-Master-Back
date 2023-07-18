from app.common.ext import mh 
from app.bodegas.model import Bodega


class BodegasSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Bodega
    
    id = mh.auto_field(dump_only=True)