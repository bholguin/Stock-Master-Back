from app.common.db import db, BaseModel


class Vehiculo(db.Model, BaseModel):
    __tablename__ = "vehiculos"
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(8))
    descripcion = db.Column(db.String(50))
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)

    def __init__(self, placa: str, descripcion: str, empresa_id: int, marca: str, modelo: str):
        self.descripcion = descripcion
        self.placa = placa
        self.empresa_id = empresa_id
        self.marca = marca,
        self.modelo = modelo

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
    def update_vehiculo(self, modelo: dict):
        vehiculo = self.get_by_id(modelo['id'])
        vehiculo.placa = modelo['placa']
        vehiculo.descripcion = modelo['descripcion']
        vehiculo.marca = modelo['marca']
        vehiculo.modelo = modelo['modelo']
        vehiculo.update()
        return vehiculo
    
    @classmethod
    def delete_vehiculo(self, id: int):
        empresa = self.get_by_id(id)
        self.delete(empresa)
        return id
