from app.common.db import db, BaseModel


class Vehiculo(db.Model, BaseModel):
    __tablename__ = "vehiculos"
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(8))
    descripcion = db.Column(db.String(50))
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)

    def __init__(self, placa: str, descripcion: str, empresa_id: int):
        self.descripcion = descripcion
        self.placa = placa
        self.empresa_id = empresa_id

    @classmethod
    def create_vehiculo(self, modelo: dict, empresa_id: int):
        vehiculo = Vehiculo(descripcion=modelo["descripcion"],
                            placa=modelo["placa"],
                            empresa_id=empresa_id)
        vehiculo.save()
        return vehiculo
