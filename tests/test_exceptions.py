import unittest
from expandobjects.exceptions import BasePyExpandObjectsException, VirtualMethodUse


class TestBasePyExpandObjectsException(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(BasePyExpandObjectsException):
            raise BasePyExpandObjectsException()


class TestVirtualMethodUse(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(VirtualMethodUse):
            raise VirtualMethodUse("a", "b")

    def test_string_repr(self):
        e = VirtualMethodUse("a", "b")
        self.assertEqual("Virtual Method Called: Class \"a\"; Method: \"b\"", str(e))
