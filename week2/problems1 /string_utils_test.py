import unittest
import string_utils


class sting_utils_test(unittest.TestCase):

    """Testing the unit"""

    def test_lines(self):
        self.assertEqual(
            ["hello", "world"], string_utils.lines("hello\nworld"))

    def test_unlines(self):
        self.assertEqual(
            'hello\nworld', string_utils.unlines(["hello", "world"]))

    def test_words(self):
        self.assertEqual(['hello', 'world'], string_utils.words('hello world'))

    def test_unword(self):
        self.assertEqual(
            'hello world', string_utils.unword(['hello', 'world']))

    def test_tab_to_spaces(self):
        self.assertEqual("hello    world", string_utils.tab_to_spaces("hello    world", 4))


if __name__ == '__main__':
    unittest.main()
