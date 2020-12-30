#Marshmallow Es una extensión que facilita la serialización de los modelos de la base de datos a JSON y viceversa
from flask_marshmallow import Marshmallow
#Esta extensión permite generar las tablas de la base de datos a partir de ficheros de migración
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager

mh = Marshmallow()
migrate = Migrate()
api = Api()
jwt = JWTManager()

