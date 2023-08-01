from app.common.db import db, BaseModel
from datetime import datetime

class Movimiento(db.Model, BaseModel):
    __tablename__ = "movimientos"
    id = db.Column(db.Integer, primary_key=True)
    creado = db.Column(db.DateTime, default=datetime.utcnow)
    cantidad = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.String(1), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)
    documento_id = db.Column(db.Integer, db.ForeignKey("documentos.id"), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    bodega_id = db.Column(db.Integer, db.ForeignKey("bodegas.id"), nullable=False)

    def __init__(self, tipo: str, cantidad: int, bodega_id: int, producto_id: int, empresa_id: int, documento_id: int, item_id: int, usuario_id: int):
        self.cantidad = cantidad
        self.producto_id = producto_id
        self.empresa_id = empresa_id
        self.documento_id = documento_id
        self.item_id = item_id
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.bodega_id = bodega_id


