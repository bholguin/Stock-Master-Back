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