from app.common.db import db, BaseModel
from app.documentos.items.models import Item
from datetime import datetime
class Documento(db.Model, BaseModel):
    __tablename__ = "documentos"
    id = db.Column(db.Integer, primary_key=True)
    creado = db.Column(db.DateTime, default=datetime.utcnow)
    consecutivo = db.Column(db.Integer)
    concepto = db.Column(db.String(30), nullable=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)
    tipodoc_id = db.Column(db.Integer, db.ForeignKey("tipos_documento.id"), nullable=False)
    bodega_id = db.Column(db.Integer, db.ForeignKey("bodegas.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey("vehiculos.id"), nullable=True)
    items = db.relationship("Item", backref="documento_item", lazy=True)
    tipodoc = db.relationship("TipoDocumento", backref="tipodoc")
    bodega = db.relationship("Bodega", backref="bodega")

    def __init__(self, consecutivo: int , empresa_id: int, tipodoc_id: int, bodega_id: int, usuario_id: int, vehiculo_id: int, concepto: str):
        self.consecutivo = consecutivo
        self.empresa_id = empresa_id
        self.tipodoc_id = tipodoc_id
        self.bodega_id = bodega_id
        self.usuario_id = usuario_id
        self.vehiculo_id = vehiculo_id
        self.concepto = concepto





