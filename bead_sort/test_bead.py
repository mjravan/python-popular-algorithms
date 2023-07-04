import unittest
import bead_sort


class BeadSort(unittest.TestCase):
    def test_non_negative(self):
        with self.assertRaises(TypeError):
            bead_sort.bead_sort([3, -2, 4, 1])

    def test_sort(self):
        actual = bead_sort.bead_sort([3, 5, 2, 6, 1])
        excepted = [1, 2, 3, 5, 6]
        self.assertEqual(actual, excepted)
