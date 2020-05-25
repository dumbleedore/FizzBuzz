import unittest
from .fizzbuzz import fizzbuzz


class Fizzbuzz_test(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertIsNone(fizzbuzz([4, True, 6, 7, 8]))


if __name__ == 'main':
    unittest.main()