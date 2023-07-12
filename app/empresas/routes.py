from app.empresas.resources import EmpresaResource, EmpresasResource, EmpresasByUsernameResource
from flask import Blueprint
from flask_restful import Api


modulo_empresa = Blueprint("modulo_empresa", __name__)
api = Api(modulo_empresa)

api.add_resource(EmpresaResource, "/api/empresa/", endpoint="empresa")
api.add_resource(EmpresasResource, "/api/empresas/", endpoint="empresas")
api.add_resource(EmpresasByUsernameResource, "/api/empresas_by_username", endpoint="empresas_by_username")
