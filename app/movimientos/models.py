from app.common.db import db, BaseModel
from datetime import datetime
from app.documentos.models import Documento
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, DateTime, Float

class Movimiento(db.Model, BaseModel):
    __tablename__ = "movimientos"
    id: Mapped[int] = mapped_column(primary_key=True)
    creado = mapped_column(DateTime, default=datetime.now(datetime.UTC))
    cantidad = mapped_column(Float)
    tipo: Mapped[str] = mapped_column(String(1))
    empresa_id = mapped_column(Integer, ForeignKey("empresas.id"))
    producto_id =  mapped_column(Integer, ForeignKey("productos.id"))
    documento_id = mapped_column(Integer, ForeignKey("documentos.id"))
    item_id = mapped_column(Integer, ForeignKey("items.id"))
    usuario_id = mapped_column(Integer, ForeignKey("usuarios.id"))
    bodega_id = mapped_column(Integer, ForeignKey("bodegas.id"))
    documento: Mapped["Documento"] = relationship(
        back_populates="documento", cascade="all, delete-orphan"
    )
    documento =  db.relationship("Documento", backref="documento")

    def __init__(self, tipo: str, cantidad: int, bodega_id: int, producto_id: int, empresa_id: int, documento_id: int, item_id: int, usuario_id: int):
        self.cantidad = cantidad
        self.producto_id = producto_id
        self.empresa_id = empresa_id
        self.documento_id = documento_id
        self.item_id = item_id
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.bodega_id = bodega_id

    @classmethod
    def get_kadex(self, empresa_id: int, producto_id: int, bodega_id: int):
        movimientos = self.query.filter(self.empresa_id==empresa_id,
                                        self.producto_id==producto_id,
                                        self.bodega_id==bodega_id).all()
        return movimientos

