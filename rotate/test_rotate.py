import unittest
import rotate


class Rotate(unittest.TestCase):
    # short sequences
    def test_short(self):
        actual = rotate.rotate('hello', 6)
        excepted = 'elloh'
        self.assertEqual(actual, excepted)

    # long sequences
    def test_long(self):
        actual = rotate.rotate('brother', 2)
        excepted = 'otherbr'
        self.assertEqual(actual, excepted)
