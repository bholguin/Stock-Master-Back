from app.common.db import db, BaseModel

class Producto(db.Model, BaseModel):
    __tablename__ = "productos"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    referencia = db.Column(db.String(30))
    descripcion = db.Column(db.String(100))
    unidad_id = db.Column(db.Integer, db.ForeignKey("unidades_medidas.id"), nullable=False)
    empresa_id = db.Column(db.Integer, db.ForeignKey("empresas.id"), nullable=False)
    unidad = db.relationship("UnidadesMedidas", backref="producto")