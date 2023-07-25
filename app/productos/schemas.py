from app.common.ext import mh 
from app.productos.models import Producto


class ProductoSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Producto
    
    id = mh.auto_field(dump_only=True)