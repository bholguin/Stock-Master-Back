from app.common.ext import mh
from app.modulos.submodulo.models import Submodulo


class SubmoduloSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Submodulo

    id = mh.auto_field(dump_only=True)




