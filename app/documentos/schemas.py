from app.common.ext import mh 
from app.documentos.models import Documento


class DocumentoSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Documento
    
    id = mh.auto_field(dump_only=True)
    tipodoc = mh.Nested('TipoDocumentoSchema')
    bodega = mh.Nested('BodegasSchema')