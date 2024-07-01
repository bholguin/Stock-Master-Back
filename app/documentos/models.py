from app.common.db import Base
from app.documentos.items.models import Item
#from app.movimientos.models import Movimiento
from app.bodegas.model import Bodega
from app.tipos_documento.models import TipoDocumento
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer, DateTime

class Documento(Base):
    __tablename__ = "documentos"
    id: Mapped[int] = mapped_column(primary_key=True)
    creado: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())
    consecutivo: Mapped[Integer] = mapped_column(Integer)
    concepto: Mapped[String] = mapped_column(String(30), nullable=True)
    empresa_id = mapped_column(Integer, ForeignKey("empresas.id"), nullable=False)
    tipodoc_id = mapped_column(Integer, ForeignKey("tipos_documento.id"), nullable=False)
    bodega_id = mapped_column(Integer, ForeignKey("bodegas.id"), nullable=False)
    usuario_id = mapped_column(Integer, ForeignKey("usuarios.id"), nullable=False)
    vehiculo_id = mapped_column(Integer, ForeignKey("vehiculos.id"), nullable=False)
    items: Mapped["Item"] = relationship(
        backref="documento_item", cascade="all, delete-orphan", lazy=True
    )
    tipodoc: Mapped["TipoDocumento"] = relationship(
        backref="tipodoc", cascade="all, delete-orphan", lazy=True
    )
    bodega: Mapped["Bodega"] = relationship(
        backref="bodega", cascade="all, delete-orphan", lazy=True
    )
    """  movimientos: Mapped["Movimiento"] = relationship(
        backref="documento_movimientos", cascade="all, delete-orphan", lazy=True
    ) """

    def __init__(self, consecutivo: int , empresa_id: int, tipodoc_id: int, bodega_id: int, usuario_id: int, vehiculo_id: int, concepto: str):
        self.consecutivo = consecutivo
        self.empresa_id = empresa_id
        self.tipodoc_id = tipodoc_id
        self.bodega_id = bodega_id
        self.usuario_id = usuario_id
        self.vehiculo_id = vehiculo_id
        self.concepto = concepto





