from app.common.db import db, BaseModel


class Vehiculo(db.Model, BaseModel):
    __tablename__ = "vehiculos"
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10))
    descripcion = db.Column(db.String(50))

    def __init__(self, placa: str, descripcion: str):
        self.descripcion = descripcion
        self.placa = placa

    @classmethod
    def create_vehiculo(self, modelo: dict):
        vehiculo = Vehiculo(descripcion=modelo["descripcion"],
                            placa=modelo["placa"])
        vehiculo.save()
        return vehiculo
