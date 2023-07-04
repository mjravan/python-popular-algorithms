import unittest
import is_isomorphic


class IsoMorphic(unittest.TestCase):
    # test strings with unequal lengths
    def test_length(self):
        actual = is_isomorphic.is_isomorphic('amir', 'cow')
        excepted = False
        self.assertEqual(actual, excepted)

    def test_not_iso(self):
        actual = is_isomorphic.is_isomorphic('amir', 'bmir')
        excepted = True
        self.assertEqual(actual, excepted)

    def test_iso(self):
        actual = is_isomorphic.is_isomorphic('paper', 'title')
        excepted = True
        self.assertEqual(actual, excepted)
