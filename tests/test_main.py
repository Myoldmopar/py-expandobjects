import unittest

from expandobjects.exceptions import InvalidCommandLineArguments
from expandobjects.main import sub_worker


class TestMainWorker(unittest.TestCase):

    def test_valid_workflow(self):
        fake_argv = ['dummy_binary_name', '/something/doesnt/exist']
        with self.assertRaises(InvalidCommandLineArguments):
            sub_worker(fake_argv, raise_exceptions=True)
