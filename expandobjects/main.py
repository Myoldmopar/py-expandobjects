import os
import sys

from expandobjects.exceptions import InvalidCommandLineArguments, FileIOProblem, ExitCodes
from expandobjects.expander import ExpansionManager


def usage(binary_name):
    return """ \
Expand template objects in EnergyPlus.  Usage:
$ %s "/path/to/my.idf" ["/path/to/expanded_file_name.idf"]
    """ % binary_name


def sub_worker(these_argv, raise_exceptions=False, print_error_messages=True):

    # there should always be one command line argument, the binary name
    # if there's not, then in that weird situation I'm OK having an unhandled exception
    # as I wouldn't know what to handle about it anyway
    binary_name = these_argv[0]

    # first check command line arguments
    if len(these_argv) < 2:  # pragma no cover
        if print_error_messages:
            print("Invalid command line arguments; needs at least one argument for the input file to expand")
            print(usage(binary_name))
        if raise_exceptions:
            raise InvalidCommandLineArguments()
        else:
            sys.exit(ExitCodes[InvalidCommandLineArguments])
    elif len(these_argv) > 3:  # pragma no cover
        if print_error_messages:
            print("Invalid command line arguments; needs at most two arguments: input file and output file")
            print(usage(binary_name))
        if raise_exceptions:
            raise InvalidCommandLineArguments()
        else:
            sys.exit(ExitCodes[InvalidCommandLineArguments])

    # *** this point on, it's only possibly for exactly 2 or 3 total command line arguments (including the binary name)

    # validate and process the first command line argument: the input file
    input_file_path = these_argv[1]
    if not os.path.exists(input_file_path):
        if print_error_messages:
            print("Invalid command line arguments; input file does not exist: \"%s\"" % input_file_path)
            print(usage(binary_name))
        if raise_exceptions:
            raise InvalidCommandLineArguments()
        else:
            sys.exit(ExitCodes[InvalidCommandLineArguments])

    # validate and process the optional second command line argument: the output file
    if len(these_argv) == 2:
        # we need to get the directory from the input file command line argument
        input_file_base_dir = os.path.dirname(input_file_path)
        output_file_path = os.path.join(input_file_base_dir, 'expanded.idf')
    else:  # 3, so the output file path is included
        output_file_path = these_argv[2]
    # try deleting it; if it doesn't exist this will quietly pass
    try:
        os.remove(output_file_path)
    except OSError:
        pass
    # if it didn't get deleted, it will still be there!
    if os.path.exists(output_file_path):
        if print_error_messages:
            print("Previous output file could not be deleted, cannot continue; file at: \"%s\"" % output_file_path)
        if raise_exceptions:
            raise FileIOProblem()
        else:
            sys.exit(ExitCodes[FileIOProblem])

    # now create file-like objects for the input and output and pass them to the main expansion engine
    in_file = open(input_file_path, 'r')
    expander = ExpansionManager()
    expander.expand(in_file)
    return ExitCodes[None]


def main():  # pragma no cover
    """This is the main command line entry point to this library.
    After a pip install, a binary will be available on the Python bin path called \"expand_objects\", which provides
    an entry point into this function.  

    Currently this function accepts two positional arguments:
    1. The name of the file to be expanded
    2. An optional output name.  If not provided, the output file will be expanded.idf (in the input file directory)

    Example usage:
    $ expand_objects /path/to/my.idf /path/to/expanded_file_name.idf
    """
    sys.exit(sub_worker(sys.argv))


if __name__ == "__main__":
    main()
