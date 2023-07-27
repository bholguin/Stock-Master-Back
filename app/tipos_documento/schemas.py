from app.common.ext import mh 
from app.tipos_documento.models import TipoDocumento


class TipoDocumentoSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = TipoDocumento
    
    id = mh.auto_field(dump_only=True)