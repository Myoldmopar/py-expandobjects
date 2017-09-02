from pyiddidf.idf.objects import IDFStructure, IDFObject


class ExpansionManager(object):
    """This class has functions for performing the actual expansion process.
    The initializer expects the input file data as the argument and returns output file text
    """

    def __init__(self):
        pass

    def expand(self, idd_structure, idf_structure):
        new_idf_structure = IDFStructure("")
        new_idf_structure.objects = []
        for object in idf_structure.objects:
            if object.object_name == 'HVACTemplate:Something':
                new_idf_object = IDFObject(['Something', 'NewField1'])
                new_idf_structure.objects.append(new_idf_object)
            else:
                new_idf_structure.objects.append(object)
        p = new_idf_structure.whole_idf_string(idd_structure)
        return p
