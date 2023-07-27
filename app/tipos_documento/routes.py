from app.tipos_documento.resources import TipoDocumentoResource, TiposDocumentoResource
from flask import Blueprint
from flask_restful import Api

modulo_tipodoc = Blueprint('modulo_tipodoc', __name__)
api = Api(modulo_tipodoc)

api.add_resource(TipoDocumentoResource, "/api/tipo-documento", endpoint="tipo-documento")
api.add_resource(TiposDocumentoResource, "/api/tipos-documento", endpoint="tipos-documento")