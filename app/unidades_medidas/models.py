from app.common.db import db, BaseModel

class UnidadesMedidas(db.Model, BaseModel):
    __tablename__ = "unidades_medidas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    prefijo = db.Column(db.String(20), nullable=False, unique=True)
    descripcion = db.Column(db.String(100))
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)


    def __init__(self, nombre: str, prefijo: str, descripcion: str, empresa_id: int):
        self.nombre = nombre
        self.prefijo = prefijo
        self.descripcion = descripcion
        self.empresa_id = empresa_id

    @classmethod
    def create_unidad(self, modelo: dict, empresa_id: int):
        print(modelo, empresa_id)
        unidad = UnidadesMedidas(nombre=modelo["nombre"],
                            prefijo=modelo["prefijo"],
                            descripcion=modelo["descripcion"],
                            empresa_id=empresa_id)
        unidad.save()
        return unidad
    
    @classmethod
    def update_unidad(self, modelo: dict):
        unidad = self.get_by_id(modelo['id'])
        unidad.nombre = modelo['nombre']
        unidad.descripcion = modelo['descripcion']
        unidad.prefijo = modelo['prefijo']
        unidad.update()
        return unidad
    
    @classmethod
    def delete_unidad(self, id: int):
        empresa = self.get_by_id(id)
        self.delete(empresa)
        return id