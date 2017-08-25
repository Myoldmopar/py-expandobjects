
class ExpansionManager(object):
    """This class has functions for performing the actual expansion process.
    The initializer expects the input file data as the argument and returns output file text
    """

    def __init__(self):
        pass

    def expand(self, input_file_text):
        output = "Hello\n"
        output += input_file_text
        return output
