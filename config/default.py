import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Para propagar las excepciones y poder manejarlas a nivel de aplicación.
    PROPAGATE_EXCEPTIONS = True
    #Deshabilita las sugerencias de otros endpoints relacionados con alguno que no exista (Flask-Restful).
    ERROR_404_HELP = False
    FLASKY_ADMIN = 'Brayhan Holguin'
    #Configuracion JWT-Extended
    JWT_ACCESS_TOKEN_EXPIRES = 3600
    JWT_BLACKLIST_ENABLED = True
    JWT_BLACKLIST_TOKEN_CHECKS = ['access']

    SWAGGER_URL = '/api/docs'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    #habilita debug
    DEBUG = True
    # Lo utilizan Flask y ciertas extensiones que manejan aspectos de seguridad.
    SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://master:inventario123!@stock-master-database.mysql.database.azure.com/app'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:App1234!@host.docker.internal:3306/app'
    #Se desactiva como indica la documentación.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Se deshabilitan los mensajes de log de SQLAlchemy.
    SHOW_SQLALCHEMY_LOG_MESSAGES = True
    

class ProductionConfig(Config):
    #habilita debug
    DEBUG = True
    # Lo utilizan Flask y ciertas extensiones que manejan aspectos de seguridad.
    SECRET_KEY = '123447a47f563e90fe2db0f56b1b17be62378e31b7cfd3adc776c59ca4c75e2fc512c15f69bb38307d11d5d17a41a7936789'
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:App1234!@127.0.0.1:3306/app'
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:App1234!@host.docker.internal:3306/app'
    #Se desactiva como indica la documentación.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #Se deshabilitan los mensajes de log de SQLAlchemy.
    SHOW_SQLALCHEMY_LOG_MESSAGES = True


class TestingConfig(Config):
    pass


config = {
 'development': DevelopmentConfig,
 'testing': TestingConfig,
 'production': ProductionConfig,
 'default': DevelopmentConfig
}
