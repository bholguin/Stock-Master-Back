from app.empresas.resources import EmpresaResource, EmpresasResource
from flask import Blueprint
from flask_restful import Api


modulo_empresa = Blueprint("modulo_empresa", __name__)
api = Api(modulo_empresa)

api.add_resource(EmpresaResource, "/api/empresa/", '/api/empresa/<int:id>', endpoint="empresa")
api.add_resource(EmpresasResource, "/api/empresas/", endpoint="empresas")