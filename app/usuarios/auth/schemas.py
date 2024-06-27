from marshmallow import Schema, fields
from app.usuarios.schemas import UsuarioSchema
from app.empresas.schemas import EmpresaSchema

class LoginSchema(Schema):

    token = fields.Str()
    usuario = fields.Nested(UsuarioSchema())
    empresa = fields.Nested(EmpresaSchema())

