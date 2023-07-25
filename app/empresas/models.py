from app.common.db import db, BaseModel
from app.vehiculos.models import Vehiculo
from app.usuarios.models import Usuario
from app.bodegas.model import Bodega
from app.productos.models import Producto
from app.unidades_medidas.models import UnidadesMedidas
from app.common.error_handling import ObjectNotFound, ForbiddenError


class Empresa(db.Model, BaseModel):
    __tablename__ = "empresas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), unique=True)
    nit = db.Column(db.String(15))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    vahiculos = db.relationship('Vehiculo', backref='vehiculo')
    usuarios = db.relationship('Usuario', backref='usuario', lazy=True)
    unidades = db.relationship('UnidadesMedidas', backref='unidades')
    bodegas = db.relationship('Bodega', backref='bodegas')
    productos = db.relationship('Producto', backref='productos', lazy=True)

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
