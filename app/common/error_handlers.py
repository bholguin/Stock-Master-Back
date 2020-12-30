from flask import jsonify
from app.common.error_handling import \
    ObjectNotFound, \
    AppErrorBaseClass, \
    LoginNotFound, \
    ForbiddenError, \
    EmptyMessage



def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception_error(e):
        return jsonify('Internal server error'), 500

    @app.errorhandler(405)
    def handle_405_error(e):
        return jsonify('Method not allowed'), 405

    @app.errorhandler(ForbiddenError)
    def handle_403_error(e):
        return jsonify('Forbidden error'), 403

    @app.errorhandler(LoginNotFound)
    def handle_401_error(e):
        return jsonify('Verifique usuario y contraseña'), 401

    @app.errorhandler(404)
    def handle_404_error(e):
        return jsonify('Not Found error'), 404

    @app.errorhandler(AppErrorBaseClass)
    def handle_app_base_error(e):
        return jsonify(str(e)), 500

    @app.errorhandler(ObjectNotFound)
    def handle_object_not_found_error(e):
        return jsonify(str(e)), 404

    @app.errorhandler(EmptyMessage)
    def handle_204_error(e):
        return jsonify('Empty Response'), 204