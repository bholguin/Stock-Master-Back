from app.common.db import Base
from app.movimientos.models import Movimiento
from app.productos.models import Producto
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Float

class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    cantidad: Mapped[Float] = mapped_column(Float, nullable=False)
    producto_id = mapped_column(Integer, ForeignKey("productos.id"), nullable=False)
    documento_id = mapped_column(Integer, ForeignKey("documentos.id"), nullable=False)
    producto: Mapped["Producto"] = relationship(
        backref="producto", cascade="all, delete-orphan", lazy=True
    )
    movimientos: Mapped["Movimiento"] = relationship(
        backref="item_movimientos", cascade="all, delete-orphan", lazy=True
    )

    def __init__(self, cantidad, producto_id: int, documento_id: int):
        self.cantidad = cantidad
        self.documento_id = documento_id
        self.producto_id = producto_id





