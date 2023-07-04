import unittest
import a1z26_cipher


class Cipher(unittest.TestCase):
    def test_encode(self):
        actual = a1z26_cipher.encode('majed')
        excepted = [109, 97, 106, 101, 100]
        self.assertEqual(actual, excepted)

    def test_decode(self):
        actual = a1z26_cipher.decode([97, 109, 105, 114])
        excepted = 'amir'
        self.assertEqual(actual, excepted)
