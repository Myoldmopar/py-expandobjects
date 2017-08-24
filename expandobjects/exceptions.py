class BasePyExpandObjectsException(Exception):
    """Base class for all PyExpandObjects related exceptions"""
    pass


class VirtualMethodUse(BasePyExpandObjectsException):
    """Raised when a pure virtual method is called instead of calling the derived class method"""
    def __init__(self, base_class_name, method_name):
        self.base_class_name = base_class_name
        self.method_name = method_name

    def __str__(self):  # pragma no cover
        return "Virtual Method Called: Class \"%s\"; Method: \"%s\"" % (self.base_class_name, self.method_name)
