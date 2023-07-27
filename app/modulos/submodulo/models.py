from app.common.db import db, BaseModel

class Submodulo(db.Model, BaseModel):
    __tablename__ = 'submodulos'
    id = db.Column(db.String(20), primary_key=True)
    go = db.Column(db.String(50))
    tipo_doc = db.Column(db.Boolean)
    modulo_id = db.Column(db.String(20), db.ForeignKey("modulos.id"), nullable=False)

    def __init__():
        pass
