from flask import Flask, jsonify
from app.common.db import db
from flask_cors import CORS
from app.common.ext import mh, migrate, jwt
from flask_restful import Api
import json
#config app
from config.default import config
#app Extension
from app.common.command import command_app
from app.common.jwt_bihavier import jwt_callbacks
from app.common.error_handlers import register_error_handlers
#blueprint modules
from flask_swagger_ui import get_swaggerui_blueprint
from app.usuarios.routes import modulo_usuarios
from app.usuarios.auth.routes import modulo_login
from app.vehiculos.routes import modulo_vehiculos
from app.empresas.routes import modulo_empresa
from app.unidades_medidas.routes import modulo_unidades_medidas
from app.validator.routes import modulo_validator
from app.bodegas.routes import modulo_bodegas
from app.productos.routes import modulo_producto
from app.modulos.routes import modulo_modulos
from app.modulos.submodulo.routes import modulo_submodulos
from app.tipos_documento.routes import modulo_tipodoc
from app.entradas.routes import modulo_entradas
from app.salidas.routes import modulo_salidas
from app.movimientos.routes import modulo_movimientos

def create_app():
    app = Flask(__name__)
    app.config.from_object(config['development'])
    config['development'].init_app(app)
    #inicializa cors
    #CORS(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)
    #Inicializa las extensiones
    db.init_app(app)
    mh.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    #Captura todos los errores 404
    Api(app, catch_all_404s=True)
    #Deshabilita el modo estricto de acabado de una URL con /
    app.url_map.strict_slashes = False

    #configuracion de swagger
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.json'
    swagger_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': 'Stock Master Api'
        }
    )

    
    #Registra los blueprints
    app.register_blueprint(modulo_empresa)
    app.register_blueprint(modulo_login)
    app.register_blueprint(modulo_usuarios)
    app.register_blueprint(modulo_vehiculos)
    app.register_blueprint(modulo_unidades_medidas)
    app.register_blueprint(modulo_validator)
    app.register_blueprint(modulo_bodegas)
    app.register_blueprint(modulo_producto)
    app.register_blueprint(modulo_modulos)
    app.register_blueprint(modulo_submodulos)
    app.register_blueprint(modulo_tipodoc)
    app.register_blueprint(modulo_entradas)
    app.register_blueprint(modulo_salidas)
    app.register_blueprint(modulo_movimientos)
    app.register_blueprint(swagger_blueprint, url_prefix = SWAGGER_URL)

    #Registra los comandos configurados en esta aplicación
    command_app(app)
    #Registra manejadores de errores personalizados
    register_error_handlers(app)
    #Callbacks de control de comportamiento de los jwt
    jwt_callbacks(jwt)
    

    return app


