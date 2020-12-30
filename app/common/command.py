from app.usuarios.models import Usuario
import click

def command_app(app):
    @app.cli.command("create-user-admin")
    @click.option('--name', prompt='Your name',
              help='add name.')
    @click.option('--lastname', prompt='Your lastname',
                help='add lastname.')
    @click.option('--username', prompt='Your username',
                help='add username.')
    @click.option('--password', prompt='Your password',
                help='add password.')
    def create_user_admin(name, lastname, username, password):
        user_admin = Usuario(
            username= username,
            password= password,
            nombre= name,
            apellido= lastname
        )
        user_admin.save()
        print('Se creo Exitosamente.')