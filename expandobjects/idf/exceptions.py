
class ProcessingException(Exception):
    """
    This exception occurs when an unexpected error occurs during the processing of an input file.
    """

    def __init__(self, message, line_index=None, object_name="", field_name=""):
        super(ProcessingException, self).__init__(message)
        self.message = message
        self.line_index = line_index

    def __str__(self):
        return "Processing Exception on line number {}; message: {}".format(self.line_index, self.message)
