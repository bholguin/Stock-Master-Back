from app.common.db import db, BaseModel
from app.modulos.submodulo.models import Submodulo

class Modulo(db.Model, BaseModel):
    __tablename__ = 'modulos'
    id = db.Column(db.String(20), primary_key=True)
    go = db.Column(db.String(50))
    submodulos = db.relationship('Submodulo', backref='submodulos', lazy=True)

    def __init__(slef):
        pass
