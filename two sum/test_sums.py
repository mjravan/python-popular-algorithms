import unittest
import two_sum


class TwoSum(unittest.TestCase):
    def test_show(self):
        actual = two_sum.two_sum([2, 7, 11, 15], 22)
        # normal counting places in list
        excepted = [2, 4]
        self.assertEqual(actual, excepted)
