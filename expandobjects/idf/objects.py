# import logging
#
# module_logger = logging.getLogger("eptransition.idd.processor")


class ValidationIssue:
    """
    This class stores information about any issue that occurred when reading an IDF file.

    :param str object_name: The object type that was being validated when this issue arose
    :param int severity: The severity of this issue, from the class constants
    :param str message: A descriptive message for this issue
    :param str field_name: The field name that was being validated when this issue arose, if available.
    """

    INFORMATION = 0
    WARNING = 1
    ERROR = 2

    def __init__(self, object_name, severity, message, field_name=None):
        self.object_name = object_name
        self.severity = severity
        self.message = message
        self.field_name = field_name

    @staticmethod
    def severity_string(severity_integer):
        """
        Returns a string version of the severity of this issue

        :param int severity_integer: One of the constants defined in this class (INFORMATION, etc.)
        :return: A string representation of the severity
        """
        if severity_integer == ValidationIssue.INFORMATION:
            return "INFORMATION"
        elif severity_integer == ValidationIssue.WARNING:
            return "*WARNING*"
        elif severity_integer == ValidationIssue.ERROR:
            return "**ERROR**"
        else:
            raise Exception("Bad integer passed into severity_string()")

    def __str__(self):
        msg = " * Issue Found; severity = " + ValidationIssue.severity_string(self.severity) + "\n"
        msg += "  Object Name = " + self.object_name + "\n"
        if self.field_name is not None:
            msg += "  Field Name = " + self.field_name + "\n"
        return msg


class IDFObject(object):
    """
    This class defines a single IDF object.  An IDF object is either a comma/semicolon delimited list of actual
    object data, or a block of line delimited comments.  Blocks of comment lines are treated as IDF objects so they can
    be intelligently written back out to a new IDF file after transition in the same location.

    Relevant members are listed here:

    :ivar str object_name: IDD Type, or name, of this object
    :ivar [str] fields: A list of strings, one per field, found for this object in the IDF file

    Constructor parameters:

    :param [str] tokens: A list of tokens defining this idf object, the first token in the list is the object type.
    :param bool comment_blob: A signal that this list is comment data, and not an actual IDF object; default is False.
                              indicating it is meaningful IDF data.
    """

    def __init__(self, tokens, comment_blob=False):
        self.comment = comment_blob
        if comment_blob:
            self.object_name = "COMMENT"
            self.fields = tokens
        else:
            self.object_name = tokens[0]
            self.fields = tokens[1:]

    def object_string(self, idd_object=None):
        """
        This function creates an intelligently formed IDF object.  If the current instance is comment data, it simply
        writes the comment block out, line delimited, otherwise it writes out proper IDF syntax.  If the matching IDD
        object is passed in as an argument, the field names are matched from that to create a properly commented
        IDF object.

        :param IDDObject idd_object: The IDDObject structure that matches this IDFObject
        :return: A string representation of the IDF object or comment block
        """
        s = ""
        if self.comment:
            for comment_line in self.fields:
                s += comment_line + "\n"
            return s
        if len(self.fields) == 0:
            s = self.object_name + ";\n"
        else:
            s = self.object_name + ",\n"
            padding_size = 25
            for index, idf_field in enumerate(self.fields):
                if index == len(self.fields) - 1:
                    terminator = ";"
                else:
                    terminator = ","
                s += "  " + (idf_field + terminator).ljust(
                    padding_size) + "!- \n"
        return s

    def write_object(self, file_object):
        """
        This function simply writes out the idf string to a file object

        :param file_object: A file-type object that responds to a write command
        :return: None
        """
        file_object.write(self.object_string())
        return None


class IDFStructure(object):
    """
    An IDF structure representation.  This includes containing all the IDF objects in the file, as well as meta data
    such as the version ID for this IDD, and finally providing worker functions for accessing the IDD data

    Relevant "public" members are listed here:

    :ivar str file_path: The path given when instantiating this IDF, not necessarily an actual path
    :ivar float version_float: The floating point representation of the version of this IDD (for 8.6.0 it is 8.6)
    :ivar [IDFObject] objects: A list of all IDF objects found in the IDF

    Constructor parameters:

    :param str file_path: A file path for this IDF; not necessarily a valid path as it is never used, just available
                          for bookkeeping purposes.
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.version_string = None
        self.version_float = None
        self.objects = None

    def get_idf_objects_by_type(self, type_to_get):
        """
        This function returns all objects of a given type found in this IDF structure instance

        :param str type_to_get: A case-insensitive object type to retrieve
        :return: A list of all objects of the given type
        """
        return [i for i in self.objects if i.object_name.upper() == type_to_get.upper()]

    def whole_idf_string(self, idd_structure=None):
        """
        This function returns a string representation of the entire IDF contents.  If the idd structure argument is
        passed in, it is passed along to object worker functions in order to generate an intelligent representation.

        :param IDDStructure idd_structure: An optional IDDStructure instance representing an entire IDD file
        :return: A string of the entire IDF contents, ready to write to a file
        """
        s = ""
        for idf_obj in self.objects:
            idd_obj = None
            s += idf_obj.object_string(idd_obj) + "\n"
        return s

    def write_idf(self, idf_path, idd_structure=None):
        """
        This function writes the entire IDF contents to a file.  If the idd structure argument is
        passed in, it is passed along to object worker functions in order to generate an intelligent representation.

        :param str idf_path: The path to the file to write
        :param IDDStructure idd_structure: An optional IDDStructure instance representing an entire IDD file
        :return: None
        """
        with open(idf_path, "w") as f:
            f.write(self.whole_idf_string(idd_structure))
        return None
