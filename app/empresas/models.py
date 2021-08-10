from app.common.db import db, BaseModel


class Empresa(db.Model, BaseModel):
    __tablename__ = "empresas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80))
    nit = db.Column(db.Integer)
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.String(15))

    def __init__(self, nombre: str, nit: int, direccion: str, telefono: str):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono

    @classmethod
    def create_empresa(self, modelo: dict):
        empresa = Empresa(nombre=modelo["nombre"],
                          nit=modelo["nit"], direccion=modelo['direccion'], telefono=modelo['telefono'])
        empresa.save()
        return empresa
