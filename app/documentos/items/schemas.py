from app.common.ext import mh 
from app.documentos.items.models import Item


class ItemSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Item
    
    id = mh.auto_field(dump_only=True)
    producto = mh.Nested("ProductoSchema")