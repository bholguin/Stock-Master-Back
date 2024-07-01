from app.common.db import Base
#from app.documentos.models import Documento
from app.common.error_handling import ObjectNotFound
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer

class Bodega(Base):
    __tablename__ = "bodegas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[String] = mapped_column(String(50), nullable=True)
    direccion: Mapped[String] = mapped_column(String(20))
    descripcion: Mapped[String] = mapped_column(String(100))
    empresa_id = mapped_column(Integer, ForeignKey("empresas.id"), nullable=False)
    """ movimientos: Mapped["Documento"] = relationship(
        backref="bodega_documentos", cascade="all, delete-orphan", lazy=True
    ) """

    def __init__(self, nombre: str, direccion: str, descripcion: str, empresa_id: int):
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion
        self.empresa_id = empresa_id

    @classmethod
    def get_bodega(self, bodega_id: int, empresa_id: int):
        bodega = self.query.filter(self.id==bodega_id, self.empresa_id == empresa_id).first()
        if bodega is None:
             raise ObjectNotFound('La bodega no existe')
        return bodega

    @classmethod
    def create_bodega(self, modelo: dict, empresa_id: int):
        bodega = Bodega(nombre=modelo["nombre"],
                        direccion=modelo["direccion"],
                        descripcion=modelo["descripcion"],
                        empresa_id=empresa_id)
        bodega.save()
        return bodega
    
    @classmethod
    def update_bodega(self, modelo: dict, empresa_id: int):
        bodega = self.get_bodega(modelo['id'], empresa_id)
        bodega.nombre = modelo['nombre']
        bodega.descripcion = modelo['descripcion']
        bodega.direccion = modelo['direccion']
        bodega.update()
        return bodega
    
    @classmethod
    def delete_bodega(self, bodega_id: int, empresa_id: int):
        bodega = self.get_bodega(bodega_id, empresa_id)
        self.delete(bodega)
        return bodega_id