from flask_restful import Resource
from app.modulos.submodulo.models import Submodulo

class SubmodulosResource(Resource):

    def get(self):
        return Submodulo.get_all()




