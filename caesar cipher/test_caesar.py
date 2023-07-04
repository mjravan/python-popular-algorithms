import unittest
import caesar_cipher


class Caesar(unittest.TestCase):
    def test_encode(self):
        actual = caesar_cipher.encrypt('amir', 4)
        excepted = 'eqmv'
        self.assertEqual(actual, excepted)

    def test_decode(self):
        actual = caesar_cipher.decrypt('RW', 4)
        excepted = 'NS'
        self.assertEqual(actual, excepted)
