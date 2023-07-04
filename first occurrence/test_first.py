import unittest
import first_occurrence


class TestFirst(unittest.TestCase):
    def test_normal(self):
        actual = first_occurrence.show([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 3)
        excepted = 3
        self.assertEqual(actual, excepted)


if __name__ == '__main__':
    unittest.main()
