from app.common.db import db, BaseModel

class Bodega(db.Model, BaseModel):
    __tablename__ = "bodegas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(20))
    descripcion = db.Column(db.String(100))
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)

    def __init__(self, nombre: str, direccion: str, descripcion: str, empresa_id: int):
        self.nombre = nombre
        self.direccion = direccion
        self.descripcion = descripcion
        self.empresa_id = empresa_id

    @classmethod
    def create_bodega(self, modelo: dict, empresa_id: int):
        bodega = Bodega(nombre=modelo["nombre"],
                        direccion=modelo["direccion"],
                        descripcion=modelo["descripcion"],
                        empresa_id=empresa_id)
        bodega.save()
        return bodega
    
    @classmethod
    def update_bodega(self, modelo: dict):
        bodega = self.get_by_id(modelo['id'])
        bodega.nombre = modelo['nombre']
        bodega.descripcion = modelo['descripcion']
        bodega.direccion = modelo['direccion']
        bodega.update()
        return bodega
    
    @classmethod
    def delete_bodega(self, id: int):
        bodega = self.get_by_id(id)
        self.delete(bodega)
        return id