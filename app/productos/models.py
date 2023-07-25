from app.common.db import db, BaseModel
from app.common.error_handling import ObjectNotFound

class Producto(db.Model, BaseModel):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    referencia = db.Column(db.String(30))
    descripcion = db.Column(db.String(100))
    unidad_id = db.Column(db.Integer, db.ForeignKey("unidades_medidas.id"), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)
    unidad = db.relationship("UnidadesMedidas", backref="producto")

    def __init__(self, nombre: str, referencia: str, descripcion: str, unidad_id: int, empresa_id: int):
        self.nombre = nombre
        self.referencia=referencia
        self.descripcion=descripcion
        self.empresa_id=empresa_id
        self.unidad_id=unidad_id

    @classmethod
    def create_producto(self, modelo: dict, empresa_id: int):
        producto = Producto(nombre=modelo["nombre"],
                            referencia=modelo["referencia"],
                            descripcion=modelo["descripcion"],
                            empresa_id=empresa_id,
                            unidad_id=modelo['unidad_id'])
        producto.save()
        return producto

    @classmethod
    def get_producto(self, producto_id: int, empresa_id: int):
        producto = self.query.filter(self.id==producto_id, self.empresa_id == empresa_id).first()
        if producto is None:
             raise ObjectNotFound('El producto no existe')
        return producto
    
    @classmethod
    def delete_producto(self, producto_id: int, empresa_id: int):
        producto = self.get_producto(producto_id, empresa_id)
        self.delete(producto)
        return producto_id
    
    @classmethod
    def update_producto(self, modelo: dict):
        producto = self.get_by_id(modelo['id'])
        producto.nombre = modelo['nombre']
        producto.descripcion = modelo['descripcion']
        producto.referencia = modelo['referencia']
        producto.unidad_id= modelo['unidad_id']
        producto.update()
        return producto