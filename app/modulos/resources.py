from flask_restful import Resource
from app.modulos.models import Modulo

class ModulosResource(Resource):

    def get(self):
        return Modulo.get_all()




