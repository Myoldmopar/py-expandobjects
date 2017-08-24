from expandobjects.exceptions import VirtualMethodUse


class BaseExpansion(object):
    """The base ExpandObjects rule class, to be derived for each expansion rule"""

    def do_json_expansion(self, input_context):
        """Virtual method for performing an expansion on JSON, should take an object and return one"""
        raise VirtualMethodUse("BaseExpansion", "do_json_expansion")

    def do_idf_expansion(self, input_context):
        """Virtual method for performing an expansion on IDF, should take some form of IDF object and return ..."""
        raise VirtualMethodUse("BaseExpansion", "do_idf_expansion")
