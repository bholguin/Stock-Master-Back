from app.common.db import db, BaseModel
from app.common.error_handling import ObjectNotFound, EmptyMessage
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

class Usuario(db.Model, BaseModel):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    id_publico = db.Column(db.String(32), index=True, unique=True)


    def __init__(self, nombre: str, apellido: str, username: str, password: str):
        self.nombre = nombre
        self.apellido = apellido
        self.generar_password(password)
        self.username = username
        self.gererar_id_publico()

    def __repr__(self):
        return f'Usuario({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'
    

    def generar_password(self, password: str):
        self.password = generate_password_hash(password)

    def gererar_id_publico(self):
        self.id_publico = str(uuid.uuid4().hex)

    @classmethod
    def create_user(self, modelo: dict):
        usuario = Usuario(nombre=modelo['nombre'],
                    apellido=modelo['apellido'],
                    password=modelo['password'],
                    username=modelo['username'])
        usuario.save()
        return usuario

    @classmethod
    def update_user(self, modelo: dict):
        user = self.valida_usuario_existe(int(modelo['id']))
        user.nombre = modelo['nombre']
        user.apellido = modelo['apellido']
        user.password = modelo['password']
        user.username = modelo['username']
        user.update()
        return user

    @classmethod
    def delete_user(self, id: int):
        user = self.valida_usuario_existe(id)
        self.delete(user)

    @classmethod
    def check_password(self, pwhash: str, password: str) -> bool:
        return check_password_hash(pwhash, password)

    @classmethod
    def update_password(self, id: int, password: str, npassword: str):
        usuario = self.get_by_id(id)
        if self.check_password(usuario.password, password):
            usuario.password = npassword
            self.update()
            raise EmptyMessage()
        raise ObjectNotFound

    @classmethod
    def valida_usuario_existe(self, id: int):
        usuario = self.get_by_id(id)
        if usuario is None:
            raise ObjectNotFound()
        return usuario

