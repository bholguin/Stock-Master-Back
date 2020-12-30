#from marshmallow import fields
from app.common.ext import mh
from app.usuarios.models import Usuario


class UsuarioSchema(mh.SQLAlchemyAutoSchema):

    class Meta:
        model = Usuario
        exclude = ["password"]

    id = mh.auto_field(dump_only=True)




