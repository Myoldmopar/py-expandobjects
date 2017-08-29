import StringIO
import unittest

from expandobjects.idf.objects import IDFObject, ValidationIssue


class TestIDFObject(unittest.TestCase):
    def test_valid_object(self):
        tokens = ["Objecttype", "object_name", "something", "", "last field with space"]
        obj = IDFObject(tokens)
        self.assertEquals("Objecttype", obj.object_name)
        self.assertEquals(4, len(obj.fields))
        obj.object_string()
        s = StringIO.StringIO()
        obj.write_object(s)
        expected_string = """Objecttype,
  object_name,             !-%20
  something,               !-%20
  ,                        !-%20
  last field with space;   !-%20
"""
        self.assertEqual(expected_string.replace('%20', ' '), s.getvalue())
        tokens = ["Objecttypenofields"]
        obj = IDFObject(tokens)
        self.assertEquals("Objecttypenofields", obj.object_name)
        obj.object_string()
        obj.write_object(s)


class TestSingleLineIDFValidation(unittest.TestCase):
    def test_valid_single_token_object_no_idd(self):
        tokens = ["SingleLineObject"]
        obj = IDFObject(tokens)
        self.assertEquals("SingleLineObject", obj.object_name)
        self.assertEquals(0, len(obj.fields))
        s = obj.object_string()
        self.assertEquals("SingleLineObject;\n", s)


class TestValidationIssue(unittest.TestCase):

    def test_validation_issue_info(self):
        self.assertIn("INFORMATION", ValidationIssue.severity_string(ValidationIssue.INFORMATION))

    def test_validation_issue_warning(self):
        self.assertIn("WARNING", ValidationIssue.severity_string(ValidationIssue.WARNING))

    def test_validation_issue_error(self):
        self.assertIn("ERROR", ValidationIssue.severity_string(ValidationIssue.ERROR))

    def test_validation_issue_bad(self):
        with self.assertRaises(Exception):
            ValidationIssue.severity_string(-999)

    def test_validation_issue_string(self):
        s = str(ValidationIssue("MyObject", ValidationIssue.ERROR, "Some message", "this field"))
        s += ""
