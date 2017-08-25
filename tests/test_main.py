import unittest

from expandobjects.main import sub_worker


class TestMainWorker(unittest.TestCase):

    def test_valid_workflow(self):
        fake_argv = ['dummy_binary_name', ]