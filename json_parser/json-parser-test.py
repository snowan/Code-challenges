import unittest
from json_parser.json_parser import JSONParser

class TestJSONParser(unittest.TestCase):

    def test_valid_json(self):
        valid_json = "{}"
        parser_valid = JSONParser(valid_json)
        with self.assertRaises(SystemExit) as context:
            parser_valid.parse()
        self.assertEqual(context.exception.code, 0)

    def test_invalid_json(self):
        invalid_json = "{"
        parser_invalid = JSONParser(invalid_json)
        with self.assertRaises(SystemExit) as context:
            parser_invalid.parse()
        self.assertEqual(context.exception.code, 1)

    def test_invalid_json_2(self):
        invalid_json = "{,}"
        parser_invalid = JSONParser(invalid_json)
        with self.assertRaises(SystemExit) as context:
            parser_invalid.parse()
        self.assertEqual(context.exception.code, 1)

    def test_invalid_json_3(self):
        invalid_json = '''{"key":"value",}'''
        parser_invalid = JSONParser(invalid_json)
        with self.assertRaises(SystemExit) as context:
            parser_invalid.parse()
        self.assertEqual(context.exception.code, 1)
    
    def test_valid_json_2(self):
        valid_json = '''{"key":"value"}'''
        parser_valid = JSONParser(valid_json)
        with self.assertRaises(SystemExit) as context:
            parser_valid.parse()
        self.assertEqual(context.exception.code, 0) 
    
    def test_valid_json_3(self):
        valid_json = '''{"key":"value","key2":"value2"}'''
        parser_valid = JSONParser(valid_json)
        with self.assertRaises(SystemExit) as context:
            parser_valid.parse()
        self.assertEqual(context.exception.code, 0)

if __name__ == '__main__':
    unittest.main()
