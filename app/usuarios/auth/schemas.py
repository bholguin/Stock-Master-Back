from marshmallow import Schema, fields
from app.usuarios.schemas import UsuarioSchema

class LoginSchema(Schema):
    status = fields.Str()
    token = fields.Str()
    account = fields.Nested(UsuarioSchema())


