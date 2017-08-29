import unittest

from expandobjects.idf.exceptions import ProcessingException


class TestProcessingException(unittest.TestCase):
    def test_raises(self):
        with self.assertRaises(ProcessingException):
            raise ProcessingException("message")

    def test_string_repr(self):
        e = ProcessingException("message")
        self.assertEqual('Processing Exception on line number None; message: message', str(e))
