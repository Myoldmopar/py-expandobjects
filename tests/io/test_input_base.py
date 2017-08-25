import unittest

from expandobjects.exceptions import VirtualMethodUse
from expandobjects.io.input_base import BaseInputProcessor


class TestExpansionBase(unittest.TestCase):
    def test_raises(self):
        e = BaseInputProcessor()
        with self.assertRaises(VirtualMethodUse):
            e.read_file()
