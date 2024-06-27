from app.common.db import db, BaseModel
from app.documentos.models import Documento
from app.common.error_handling import ObjectNotFound
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, Integer
from typing import List, Optional

class Vehiculo(db.Model, BaseModel):
    __tablename__ = "vehiculos"
    id: Mapped[int] = mapped_column(primary_key=True)
    placa: Mapped[str] = mapped_column(String(8))
    descripcion: Mapped[Optional[str]]
    marca: Mapped[Optional[str]]
    modelo: Mapped[Optional[str]]
    empresa_id = mapped_column(Integer, ForeignKey("empresas.id"))
    documentos: Mapped[List["Documento"]] = relationship(
        back_populates="vehiculo_documentos", cascade="all, delete-orphan"
    )

    def __init__(self, placa: str, descripcion: str, empresa_id: int, marca: str, modelo: str):
        self.descripcion = descripcion
        self.placa = placa
        self.empresa_id = empresa_id
        self.marca = marca,
        self.modelo = modelo
    
    @classmethod
    def get_vehiculo(self, vehiculo_id: int, empresa_id: int):
        vehiculo = self.query.filter(self.id==vehiculo_id, self.empresa_id == empresa_id).first()
        if vehiculo is None:
             raise ObjectNotFound('El vehiculo no existe')
        return vehiculo

    @classmethod
    def create_vehiculo(self, modelo: dict, empresa_id: int):
        vehiculo = Vehiculo(descripcion=modelo["descripcion"],
                            placa=modelo["placa"],
                            marca=modelo['marca'],
                            modelo=modelo['modelo'],
                            empresa_id=empresa_id)
        vehiculo.save()
        return vehiculo
    
    @classmethod
    def update_vehiculo(self, modelo: dict, empresa_id: int):
        vehiculo = self.get_vehiculo(modelo['id'], empresa_id)
        vehiculo.placa = modelo['placa']
        vehiculo.descripcion = modelo['descripcion']
        vehiculo.marca = modelo['marca']
        vehiculo.modelo = modelo['modelo']
        vehiculo.update()
        return vehiculo
    
    @classmethod
    def delete_vehiculo(self, vehiculo_id: int, empresa_id: int):
        empresa = self.get_vehiculo(vehiculo_id, empresa_id)
        self.delete(empresa)
        return vehiculo_id
