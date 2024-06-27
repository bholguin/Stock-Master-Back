#Para interactuar con la base de datos a través de su ORM
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

db = SQLAlchemy()

class BaseModel(DeclarativeBase):

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def update(cls):
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def filter_first(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()
