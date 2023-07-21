from app.usuarios.models import Usuario
from app.empresas.models import Empresa
import click

def command_app(app):
    @app.cli.command("create_business")
    @click.option('--business_name', prompt='Your Business name',
              help='Business name.')
    @click.option('--name', prompt='Your name',
              help='add name.')
    @click.option('--lastname', prompt='Your lastname',
                help='add lastname.')
    @click.option('--username', prompt='Your username',
                help='add username.')
    @click.option('--password', prompt='Your password',
                help='add password.')
    def create_business(business_name, name, lastname, username, password):
        empresa = Empresa(
            business_name,
            None,
            None,
            None
        )
        empresa.save()
        user_admin = Usuario(
            username= username,
            password= password,
            nombre= name,
            apellido= lastname,
            empresa_id= empresa.id,
            correo=None,
            identificacion=None,
            telefono=None
        )
        user_admin.save()
        print('Se creo Exitosamente.')