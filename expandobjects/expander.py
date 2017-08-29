from expandobjects.idf.processor import IDFProcessor
from expandobjects.idf.objects import IDFStructure, IDFObject


class ExpansionManager(object):
    """This class has functions for performing the actual expansion process.
    The initializer expects the input file data as the argument and returns output file text
    """

    def __init__(self):
        pass

    def expand(self, input_file_text):
        processor = IDFProcessor()
        idf_structure = processor.process_file_via_string(input_file_text)
        new_idf_structure = IDFStructure("")
        new_idf_structure.objects = []
        for object in idf_structure.objects:
            if object.object_name == 'HVACTemplate:Something':
                new_idf_object = IDFObject(['Something,NewField1'])
                new_idf_structure.objects.append(new_idf_object)
            else:
                new_idf_structure.objects.append(object)
        p = new_idf_structure.whole_idf_string()
        return p
