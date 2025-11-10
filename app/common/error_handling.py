class AppErrorBaseClass(Exception):
    pass
class ObjectNotFound(AppErrorBaseClass):
    pass
class LoginNotFound(AppErrorBaseClass):
    pass
class ForbiddenError(AppErrorBaseClass):
    pass
class EmptyMessage(AppErrorBaseClass):
    pass

class InvalidUsage(AppErrorBaseClass):
    def __init__(self, message="Uso inválido"):
        self.message = message
        super().__init__(self.message)