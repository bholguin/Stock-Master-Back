from app.common.ext import mh 
from app.unidades_medidas.models import UnidadesMedidas


class UnidadesMedidasSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = UnidadesMedidas
    
    id = mh.auto_field(dump_only=True)