from app.common.db import Base
#from app.productos.models import Producto
from app.common.error_handling import ObjectNotFound
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer
# from typing import List

class UnidadesMedidas(Base):
    __tablename__ = "unidades_medidas"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    prefijo: Mapped[str] = mapped_column(String(20))
    descripcion: Mapped[str] = mapped_column(String(100))
    empresa_id: Mapped[int] = mapped_column(Integer, ForeignKey("empresas.id"))
    """ productos: Mapped[List["Producto"]] = relationship(
        backref="unidades_productos", cascade="all, delete-orphan"
    ) """

    def __init__(self, nombre: str, prefijo: str, descripcion: str, empresa_id: int):
        self.nombre = nombre
        self.prefijo = prefijo
        self.descripcion = descripcion
        self.empresa_id = empresa_id

    @classmethod
    def get_unidad(self, unidad_id: int, empresa_id: int):
        unidad = self.query.filter(self.id==unidad_id, self.empresa_id == empresa_id).first()
        if unidad is None:
             raise ObjectNotFound('El unidad de medida no existe')
        return unidad

    @classmethod
    def create_unidad(self, modelo: dict, empresa_id: int):
        unidad = UnidadesMedidas(nombre=modelo["nombre"],
                            prefijo=modelo["prefijo"],
                            descripcion=modelo["descripcion"],
                            empresa_id=empresa_id)
        unidad.save()
        return unidad
    
    @classmethod
    def update_unidad(self, modelo: dict, empresa_id: int):
        unidad = self.get_unidad(modelo['id'], empresa_id)
        unidad.nombre = modelo['nombre']
        unidad.descripcion = modelo['descripcion']
        unidad.prefijo = modelo['prefijo']
        unidad.update()
        return unidad
    
    @classmethod
    def delete_unidad(self, unidad_id: int, empresa_id: int):
        unidad = self.get_unidad(unidad_id, empresa_id)
        self.delete(unidad)
        return unidad_id