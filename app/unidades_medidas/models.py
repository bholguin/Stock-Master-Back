from app.common.db import db, BaseModel
from app.productos.models import Producto
from app.common.error_handling import ObjectNotFound

class UnidadesMedidas(db.Model, BaseModel):
    __tablename__ = "unidades_medidas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    prefijo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(100))
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)
    productos = db.relationship('Producto', backref='unidades_productos', lazy=True)

    def __init__(self, nombre: str, prefijo: str, descripcion: str, empresa_id: int):
        self.nombre = nombre
        self.prefijo = prefijo
        self.descripcion = descripcion
        self.empresa_id = empresa_id

    @classmethod
    def get_unidad(self, unidad_id: int, empresa_id: int):
        unidad = self.query.filter(self.id==unidad_id, self.empresa_id == empresa_id).first()
        if unidad is None:
             raise ObjectNotFound('El unidad de medida no existe')
        return unidad

    @classmethod
    def create_unidad(self, modelo: dict, empresa_id: int):
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
    def delete_unidad(self, unidad_id: int, empresa_id: int):
        unidad = self.get_unidad(unidad_id, empresa_id)
        self.delete(unidad)
        return unidad_id