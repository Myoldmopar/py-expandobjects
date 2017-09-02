import os
import tempfile
import unittest

from expandobjects.exceptions import ExitCodes, InvalidCommandLineArguments
from expandobjects.main import sub_worker, usage


class TestMainWorker(unittest.TestCase):

    def setUp(self):

        self.binary_name = 'expand_objects'

    def test_invalid_workflow_command_line_arg_count(self):

        fake_argv = [self.binary_name]
        self.assertEqual(
            ExitCodes[InvalidCommandLineArguments],
            sub_worker(fake_argv, raise_exceptions=False, print_error_messages=False)
        )
        with self.assertRaises(InvalidCommandLineArguments):
            sub_worker(fake_argv, raise_exceptions=True, print_error_messages=False)

        fake_argv = [self.binary_name, '/still/not/enough']
        self.assertEqual(
            ExitCodes[InvalidCommandLineArguments],
            sub_worker(fake_argv, raise_exceptions=False, print_error_messages=False)
        )
        with self.assertRaises(InvalidCommandLineArguments):
            sub_worker(fake_argv, raise_exceptions=True, print_error_messages=False)

        fake_argv = [self.binary_name, 'just', 'way', 'too', 'many']
        self.assertEqual(
            ExitCodes[InvalidCommandLineArguments],
            sub_worker(fake_argv, raise_exceptions=False, print_error_messages=False)
        )
        with self.assertRaises(InvalidCommandLineArguments):
            sub_worker(fake_argv, raise_exceptions=True, print_error_messages=False)

    def test_invalid_workflow_paths_dont_exist(self):

        # first an invalid idd
        fake_argv = [self.binary_name, '/idd/doesnt/exist', '/something/doesnt/exist']
        self.assertEqual(
            ExitCodes[InvalidCommandLineArguments],
            sub_worker(fake_argv, raise_exceptions=False, print_error_messages=False)
        )
        with self.assertRaises(InvalidCommandLineArguments):
            sub_worker(fake_argv, raise_exceptions=True, print_error_messages=False)

        # then an invalid idf
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        support_file_dir = os.path.join(cur_dir, "support_files")
        fake_argv = [self.binary_name, os.path.join(support_file_dir, 'Fake.idd'), '/something/doesnt/exist']
        self.assertEqual(
            ExitCodes[InvalidCommandLineArguments],
            sub_worker(fake_argv, raise_exceptions=False, print_error_messages=False)
        )
        with self.assertRaises(InvalidCommandLineArguments):
            sub_worker(fake_argv, raise_exceptions=True, print_error_messages=False)

    def test_valid_workflow(self):

        cur_dir = os.path.dirname(os.path.realpath(__file__))
        support_file_dir = os.path.join(cur_dir, "support_files")
        fake_argv = [
            self.binary_name,
            os.path.join(support_file_dir, 'Fake.idd'),
            os.path.join(support_file_dir, 'template.idf')
        ]
        sub_worker(fake_argv, raise_exceptions=True)
        pass

    def test_expanded_file_path_arg(self):

        # valid first
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        support_file_dir = os.path.join(cur_dir, "support_files")
        handle, t = tempfile.mkstemp()
        fake_argv = [
            self.binary_name,
            os.path.join(support_file_dir, 'Fake.idd'),
            os.path.join(support_file_dir, 'template.idf'),
            t
        ]
        sub_worker(fake_argv, raise_exceptions=True)
        pass

    def test_usage(self):
        output = usage(self.binary_name)
        self.assertIn(self.binary_name, output)
