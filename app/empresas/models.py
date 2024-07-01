from app.common.db import Base
from app.vehiculos.models import Vehiculo
from app.usuarios.models import Usuario
from app.bodegas.model import Bodega
from app.productos.models import Producto
from app.unidades_medidas.models import UnidadesMedidas
from app.tipos_documento.models import TipoDocumento
from app.documentos.models import Documento
from app.movimientos.models import Movimiento
from app.common.error_handling import ObjectNotFound, ForbiddenError
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import Optional, List


class Empresa(Base):
    __tablename__ = "empresas"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str]  = mapped_column(String(80), unique=True)
    nit: Mapped[str]  = mapped_column(String(15))
    direccion: Mapped[Optional[str]]
    telefono: Mapped[Optional[str]]
    vehiculos: Mapped[List["Vehiculo"]] = relationship(
        backref="vehiculo", cascade="all, delete-orphan"
    )
    usuarios: Mapped[List["Usuario"]] = relationship(
        backref="usuario", cascade="all, delete-orphan"
    )
    unidades: Mapped[List["UnidadesMedidas"]] = relationship(
        backref="unidades", cascade="all, delete-orphan"
    )
    bodegas: Mapped[List["Bodega"]] = relationship(
        backref="bodegas", cascade="all, delete-orphan"
    )
    productos: Mapped[List["Producto"]] = relationship(
        backref="productos", cascade="all, delete-orphan"
    )
    tipos_documento: Mapped[List["TipoDocumento"]] = relationship(
        backref="empresa_tipodoc", cascade="all, delete-orphan"
    )
    documentos: Mapped[List["Documento"]] = relationship(
        backref="empresa_documentos", cascade="all, delete-orphan"
    )
    movimientos: Mapped[List["Movimiento"]] = relationship(
        backref="empresa_movimientos", cascade="all, delete-orphan"
    )

    def __init__(self, nombre: str, nit: int, direccion: str, telefono: str):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono

    @classmethod
    def create_empresa(self, modelo: dict):
        empresa = Empresa(nombre=modelo["nombre"],
                          nit=modelo["nit"],
                          direccion=modelo['direccion'],
                          telefono=modelo['telefono'])
        empresa.save()
        return empresa

    @classmethod
    def update_empresa(self, modelo: dict, id: int):
        empresa = self.valida_empresa_existe(id)
        empresa.nombre = modelo['nombre']
        empresa.nit = modelo['nit']
        empresa.direccion = modelo['direccion']
        empresa.telefono = modelo['telefono']
        empresa.update()
        return empresa

    @classmethod
    def delete_empresa(self, id: int):
        empresa = self.valida_empresa_existe(id)
        self.delete(empresa)

    @classmethod
    def get_empresas_por_username(self, username: str):
        if username is None:
            raise ForbiddenError()
        empresas = self.query.filter(self.usuarios.any(username=username)).all()
        if len(empresas) == 0:
            raise ForbiddenError()
        return empresas


    @classmethod
    def valida_empresa_existe(self, id: int):
        empresa = self.get_by_id(id)
        if empresa is None:
            raise ObjectNotFound()
        return empresa
