import unittest
from demofunction import count_words


class TestWordCount(unittest.TestCase):

    def test_case1(self):
        result = count_words("This is Python code.")
        self.assertEqual(result, 4)

    def test_case2(self):
        result = count_words("Python is cool.")
        self.assertEqual(result, 3)

    # Add more test cases here


if __name__ == '__main__':
    unittest.main()
