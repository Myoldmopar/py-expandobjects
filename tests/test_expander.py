from pyiddidf.idd.processor import IDDProcessor
from pyiddidf.idf.processor import IDFProcessor
import unittest

from expandobjects.expander import ExpansionManager


class TestExpander(unittest.TestCase):
    def test_simple_expansion(self):
        idd_text = """
        !IDD_Version 34.7.0
        !IDD_BUILD asdfadasd
        \\group Simulation Parameters
        
        Version,
          A1; \\field Version Identifier
        
        HVACTemplate:Something,
          A1, \\field Field 1
          A2; \\field Field 2
        
        Something,
          A1; \\field Field 1 Again
        """
        idd_structure = IDDProcessor().process_file_via_string(idd_text)
        idf_text = 'Version,34.7;HVACTemplate:Something,Field1,Field2;'
        idf_structure = IDFProcessor().process_file_via_string(idf_text)
        em = ExpansionManager()
        expected_text = '\n'.join([
            "Version,",
            "  34.7;                    !- ",
            "",
            "Something,",
            "  NewField1;               !- ",
            "",
            ""])
        output_text = em.expand(idf_structure, idd_structure)
        self.assertEqual(expected_text, output_text)
