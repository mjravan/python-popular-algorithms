import unittest
import binary_search


class BinarySearch(unittest.TestCase):
    def test_search(self):
        actual = binary_search.binary_search([2, 3, 4, 6, 17, 19, 21], 4)
        excepted = 2
        self.assertEqual(actual, excepted)

    def test_doesnt_exit(self):
        actual = binary_search.binary_search([2, 3, 4, 6, 17, 19, 21], 18)
        excepted = -1
        self.assertEqual(actual, excepted)
