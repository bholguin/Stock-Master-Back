from app.common.ext import mh
from app.modulos.submodulo.models import Submodulo


class SubmoduloSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Submodulo
        include_fk = True
        #include_relationships = True

    id = mh.auto_field(dump_only=True)




