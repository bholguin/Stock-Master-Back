from app.common.db import db, BaseModel
from app.documentos.models import Documento
from app.movimientos.models import Movimiento
from app.common.error_handling import ObjectNotFound, EmptyMessage
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model, BaseModel):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    username = db.Column(db.String(50))
    password = db.Column(db.String(255))
    correo = db.Column(db.String(50))
    identificacion = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    empresa_id = db.Column(db.Integer, db.ForeignKey(
        "empresas.id"), nullable=False)
    documentos = db.relationship('Documento', backref='usuario_documentos')
    movimientos = db.relationship('Movimiento', backref='usuario_movimientos')

    def __init__(self, nombre: str, apellido: str, username: str, password: str, empresa_id: int, correo: str, identificacion: str, telefono: str):
        self.nombre = nombre
        self.apellido = apellido
        self.generar_password(password)
        self.username = username
        self.empresa_id = empresa_id
        self.correo = correo
        self.telefono = telefono
        self.identificacion = identificacion

    def __repr__(self):
        return f'Usuario({self.nombre})'

    def __str__(self):
        return f'{self.nombre}'

    def generar_password(self, password: str):
        self.password = generate_password_hash(password)

    @classmethod
    def create_user(self, modelo: dict, empresa_id: int):
        password='123456'
        usuario = Usuario(nombre=modelo['nombre'],
                          apellido=modelo['apellido'],
                          password=password,
                          username=modelo['username'],
                          correo=modelo['correo'],
                          identificacion=modelo['identificacion'],
                          telefono=modelo['telefono'],
                          empresa_id=empresa_id)
        usuario.save()
        return usuario
    
    @classmethod
    def get_users(self, user_id: int, empresa_id: int):
         usuarios = self.query.filter(self.id!=user_id, self.empresa_id==empresa_id).all()
         return usuarios
    
    @classmethod
    def get_user(self, user_id: int, empresa_id: int):
         usuario = self.query.filter(self.id==user_id, self.empresa_id == empresa_id).first()
         if usuario is None:
             raise ObjectNotFound('El usuario no existe')
         return usuario

    @classmethod
    def update_user(self, modelo: dict, empresa_id: int):
        user = self.valida_usuario_existe(modelo['id'], empresa_id)
        user.nombre = modelo['nombre']
        user.apellido = modelo['apellido']
        user.username = modelo['username']
        user.correo = modelo['correo']
        user.telefono = modelo['telefono']
        user.identificacion = modelo['identificacion']
        user.update()
        return user

    @classmethod
    def delete_user(self, id: int, empresa_id: int):
        user = self.valida_usuario_existe(id, empresa_id)
        self.delete(user)

    @classmethod
    def check_password(self, pwhash: str, password: str) -> bool:
        return check_password_hash(pwhash, password)

    @classmethod
    def update_password(self, modelo: dict, id: int):
        usuario = self.get_by_id(id)
        if self.check_password(usuario.password, modelo['password'])  :
            usuario.password = generate_password_hash(modelo['newPassword'])
            self.update()
            raise EmptyMessage()
        raise ObjectNotFound()

    @classmethod
    def valida_usuario_existe(self, id, empresa_id: int):
        usuario = self.query.filter(self.id==id, self.empresa_id==empresa_id).first()
        if usuario is None:
            raise ObjectNotFound('Usuario no encontrado')
        return usuario
