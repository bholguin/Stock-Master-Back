from app.common.db import db, Base
from app.tipos_documento.models import TipoDocumento
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Boolean, ForeignKey

class Submodulo(db.Model, Base):
    __tablename__ = 'submodulos'
    id: Mapped[String] = mapped_column(String(20), primary_key=True)
    go: Mapped[String] = mapped_column(String(50))
    tipo_doc: Mapped[Boolean] = mapped_column(Boolean)
    modulo_id = mapped_column(String(20), ForeignKey("modulos.id"), nullable=False)
    tipos_documento: Mapped["TipoDocumento"] = relationship(
        backref="submodulo_tipodoc", cascade="all, delete-orphan", lazy=True
    )

    def __init__(init):
        pass
