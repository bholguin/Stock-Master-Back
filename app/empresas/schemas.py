from app.common.ext import mh 
from app.empresas.models import Empresa


class EmpresaSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Empresa
    
    id = mh.auto_field(dump_only=True)