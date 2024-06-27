from app.common.db import db, BaseModel
from app.documentos.items.models import Item
from app.movimientos.models import Movimiento
from app.unidades_medidas.models import UnidadesMedidas
from app.common.error_handling import ObjectNotFound
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer
from typing import List

class Producto(db.Model, BaseModel):
    __tablename__ = "productos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(50))
    referencia: Mapped[str] = mapped_column(String(30))
    descripcion: Mapped[str] = mapped_column(String(100))
    empresa_id = mapped_column(Integer, ForeignKey("empresas.id"))
    unidad_id = mapped_column(Integer, ForeignKey("unidades_medidas.id"))
    unidad: Mapped[List["UnidadesMedidas"]] = relationship(
        back_populates="producto", cascade="all, delete-orphan"
    )
    items: Mapped[List["Item"]] = relationship(
        back_populates="producto_item", cascade="all, delete-orphan"
    )
    movimientos: Mapped[List["Movimiento"]] = relationship(
        back_populates="productos_movimientos", cascade="all, delete-orphan"
    )

    def __init__(self, nombre: str, referencia: str, descripcion: str, unidad_id: int, empresa_id: int):
        self.nombre = nombre
        self.referencia=referencia
        self.descripcion=descripcion
        self.empresa_id=empresa_id
        self.unidad_id=unidad_id

    @classmethod
    def create_producto(self, modelo: dict, empresa_id: int):
        producto = Producto(nombre=modelo["nombre"],
                            referencia=modelo["referencia"],
                            descripcion=modelo["descripcion"],
                            empresa_id=empresa_id,
                            unidad_id=modelo['unidad_id'])
        producto.save()
        return producto

    @classmethod
    def get_producto(self, producto_id: int, empresa_id: int):
        producto = self.query.filter(self.id==producto_id, self.empresa_id==empresa_id).first()
        if producto is None:
             raise ObjectNotFound('El producto no existe')
        return producto
    
    @classmethod
    def delete_producto(self, producto_id: int, empresa_id: int):
        producto = self.get_producto(producto_id, empresa_id)
        self.delete(producto)
        return producto_id
    
    @classmethod
    def update_producto(self, modelo: dict, empresa_id: int):
        producto = self.get_producto(modelo['id'], empresa_id)
        producto.nombre = modelo['nombre']
        producto.descripcion = modelo['descripcion']
        producto.referencia = modelo['referencia']
        producto.unidad_id= modelo['unidad_id']
        producto.update()
        return producto