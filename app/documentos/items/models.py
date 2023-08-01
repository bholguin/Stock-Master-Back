from app.common.db import db, BaseModel
from app.movimientos.models import Movimiento
class Item(db.Model, BaseModel):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Float, nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    documento_id = db.Column(db.Integer, db.ForeignKey("documentos.id"), nullable=False)
    producto = db.relationship("Producto", backref="producto")
    movimientos = db.relationship('Movimiento', backref='item_movimientos')

    def __init__(self, cantidad, producto_id: int, documento_id: int):
        self.cantidad = cantidad
        self.documento_id = documento_id
        self.producto_id = producto_id





