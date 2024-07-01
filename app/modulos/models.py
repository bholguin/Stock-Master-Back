from app.common.db import db, Base
from app.modulos.submodulo.models import Submodulo
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

class Modulo(db.Model, Base):
    __tablename__ = 'modulos'
    id: Mapped[String] = mapped_column(String(20), primary_key=True)
    go: Mapped[String] = mapped_column(String(50))
    submodulos: Mapped["Submodulo"] = relationship(
        backref="submodulos", cascade="all, delete-orphan"
    )

    def __init__(slef):
        pass

    @classmethod
    def modulos_with_document(self):
        modulos = self.query.filter(self.submodulos.any(tipo_doc=True)).all()
        return modulos