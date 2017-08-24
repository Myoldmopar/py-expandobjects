from expandobjects.exceptions import VirtualMethodUse


class BaseInputProcessor(object):
    """The base input processor class, to be derived for IDF and JSON classes"""

    def read_file(self):
        """Base read_file definition; will need to add arguments and such"""
        raise VirtualMethodUse("BaseInputProcessor", "read_file")
