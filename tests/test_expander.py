import unittest

from expandobjects.expander import ExpansionManager


class TestExpander(unittest.TestCase):
    def test_simple_expansion(self):
        input_object = 'Version,8.7;HVACTemplate:Something,Field1,Field2;'
        em = ExpansionManager()
        expected_text = '\n'.join([
            "Version,",
            "  8.7;                     !- ",
            "",
            "Something,NewField1;",
            "",
            ""])
        output_text = em.expand(input_object)
        self.assertEqual(expected_text, output_text)
