import unittest
import serach_insert


class SearchInsert(unittest.TestCase):
    def test_insert(self):
        actual = serach_insert.search_insert([1, 3, 5, 6], 7)
        excepted = 4
        self.assertEqual(actual, excepted)
