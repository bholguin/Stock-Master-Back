from app.common.db import db, BaseModel
from app.productos.models import Producto
from app.documentos.models import Documento
from app.common.error_handling import ObjectNotFound

class TipoDocumento(db.Model, BaseModel):
    __tablename__ = "tipos_documento"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    prefijo = db.Column(db.String(20), nullable=False)
    descripcion = db.Column(db.String(100))
    consecutivo = db.Column(db.Integer)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)
    submodulo_id = db.Column(db.String(20), db.ForeignKey("submodulos.id"), nullable=False)
    documentos = db.relationship('Documento', backref='tipodoc_documentos')

    def __init__(self, nombre: str, prefijo: str, descripcion: str, consecutivo: int, submodulo_id: str,  empresa_id: int):
        self.nombre = nombre
        self.prefijo = prefijo
        self.descripcion = descripcion
        self.empresa_id = empresa_id
        self.consecutivo = consecutivo
        self.submodulo_id = submodulo_id

    @classmethod
    def get_tipo_doc(self, tipodoc_id: int, empresa_id: int):
        tipodoc = self.query.filter(self.id==tipodoc_id, self.empresa_id == empresa_id).first()
        if tipodoc is None:
             raise ObjectNotFound('El tipo de documento no existe')
        return tipodoc

    @classmethod
    def create_tipodoc(self, modelo: dict, empresa_id: int):
        tipodoc = TipoDocumento(nombre=modelo["nombre"],
                            prefijo=modelo["prefijo"],
                            descripcion=modelo["descripcion"],
                            consecutivo=modelo["consecutivo"],
                            submodulo_id=modelo['submodulo_id'],
                            empresa_id=empresa_id)
        tipodoc.save()
        return tipodoc
    
    @classmethod
    def update_tipodoc(self, modelo: dict, empresa_id: int):
        tipodoc = self.get_tipo_doc(modelo['id'], empresa_id)
        tipodoc.nombre = modelo['nombre']
        tipodoc.descripcion = modelo['descripcion']
        tipodoc.prefijo = modelo['prefijo']
        tipodoc.consecutivo= modelo["consecutivo"]
        tipodoc.submodulo_id= modelo["submodulo_id"]
        tipodoc.update()
        return tipodoc
    
    @classmethod
    def delete_tipodoc(self, tipodoc_id: int, empresa_id: int):
        tipodoc = self.get_tipo_doc(tipodoc_id, empresa_id)
        self.delete(tipodoc)
        return tipodoc_id