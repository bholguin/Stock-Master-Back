from app.common.db import db, BaseModel



class UnidadesMedidas(db.Model, BaseModel):
    __tablename__ = "unidades_medidas"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False, unique=True)
    prefijo = db.Column(db.String(20), nullable=False, unique=True)
    descripcion = db.Column(db.String(100))


    def __init__(self, nombre: str, prefijo: str, descripcion: str):
        self.nombre = nombre
        self.prefijo = prefijo
        self.description = descripcion