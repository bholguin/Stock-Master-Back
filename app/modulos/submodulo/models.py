from app.common.db import db, BaseModel
from app.tipos_documento.models import TipoDocumento

class Submodulo(db.Model, BaseModel):
    __tablename__ = 'submodulos'
    id = db.Column(db.String(20), primary_key=True)
    go = db.Column(db.String(50))
    tipo_doc = db.Column(db.Boolean)
    modulo_id = db.Column(db.String(20), db.ForeignKey("modulos.id"), nullable=False)
    tipos_documento = db.relationship('TipoDocumento', backref='submodulo_tipodoc', lazy=True)

    def __init__(init):
        pass
