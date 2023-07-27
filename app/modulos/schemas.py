from app.common.ext import mh
from app.modulos.models import Modulo


class ModuloSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Modulo

    id = mh.auto_field(dump_only=True)




