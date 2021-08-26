from app.common.db import db, BaseModel
from app.common.error_handling import ObjectNotFound


class Empresa(db.Model, BaseModel):
    __tablename__ = "empresas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    nit = db.Column(db.Integer)
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(15))
    folder_id = db.Column(db.String(30))

    def __init__(self, nombre: str, nit: int, direccion: str, telefono: str, folder_id: str):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.folder_id = folder_id

    @classmethod
    def create_empresa(self, modelo: dict):
        empresa = Empresa(nombre=modelo["nombre"],
                          nit=modelo["nit"],
                          direccion=modelo['direccion'],
                          telefono=modelo['telefono'],
                          folder_id=modelo['folder_id'])
        empresa.save()
        return empresa

    @classmethod
    def update_empresa(self, modelo: dict):
        empresa = self.valida_empresa_existe(int(modelo['id']))
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
    def valida_empresa_existe(self, id: int):
        empresa = self.get_by_id(id)
        if empresa is None:
            raise ObjectNotFound()
        return empresa
