import unittest
from expandobjects.io.input_base import BaseInputProcessor
from expandobjects.exceptions import VirtualMethodUse


class TestExpansionBase(unittest.TestCase):

    def test_raises(self):
        e = BaseInputProcessor()
        with self.assertRaises(VirtualMethodUse):
            e.read_file()
