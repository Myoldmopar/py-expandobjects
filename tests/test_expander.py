import unittest

from expandobjects.expander import ExpansionManager


class TestExpander(unittest.TestCase):

    def test_simple_expansion(self):
        input_object = 'World'
        em = ExpansionManager()
        output_text = em.expand(input_object)
        self.assertEqual('Hello\nWorld', output_text)
