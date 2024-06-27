from flask_restful import request, Resource
from app.empresas.models import Empresa
from app.empresas.schemas import EmpresaSchema
from app.common.ext import oidc
from flask_jwt_extended import get_current_user

empresa_schema = EmpresaSchema()


class EmpresasByUsernameResource(Resource):

    def get(self):
        username = request.args['username']
        empresas = Empresa.get_empresas_por_username(username)
        return empresa_schema.dump(empresas, many=True), 200


class EmpresasResource(Resource):

    @oidc.require_login
    def get(self):
        empresas = Empresa.get_all()
        return empresa_schema.dump(empresas, many=True)


class EmpresaResource(Resource):

    @oidc.require_login
    def get(self):
        user = get_current_user()
        empresa = Empresa.valida_empresa_existe(user.empresa_id)
        return empresa_schema.dump(empresa), 200

    @oidc.require_login
    def post(self):
        empresa = Empresa.create_empresa(request.get_json())
        return empresa_schema.dump(empresa), 200

    @oidc.require_login
    def put(self):
        user = get_current_user()
        empresa = Empresa.update_empresa(request.get_json(), user.empresa_id)
        return empresa_schema.dump(empresa), 200
