import unittest

from expandobjects.exceptions import VirtualMethodUse
from expandobjects.expansions.expansion_base import BaseExpansion


class TestExpansionBase(unittest.TestCase):
    def test_raises(self):
        e = BaseExpansion()
        with self.assertRaises(VirtualMethodUse):
            e.do_json_expansion(None)
        with self.assertRaises(VirtualMethodUse):
            e.do_idf_expansion(None)
