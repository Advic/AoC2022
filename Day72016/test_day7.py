import unittest

# noinspection PyUnresolvedReferences
from day7 import *

TEST_DATA = open('test_data.txt').read()

PART1_EXPECTED = None
PART2_EXPECTED = None


class TestDay7(unittest.TestCase):
    def test_supportsTLS(self):
        self.assertEqual(False, supportsTLS(""))
        self.assertEqual(True, supportsTLS("abba"))
        self.assertEqual(True, supportsTLS("abba[mnop]qrst"))
        self.assertEqual(False, supportsTLS("abcd[bddb]xyyx"))
        self.assertEqual(False, supportsTLS("aaaa[qwer]tyui"))
        self.assertEqual(True, supportsTLS("ioxxoj[asdfgh]zxcvbn"))

    def test_supportsSSL(self):
        self.assertEqual(True, supportsSSL("aba[bab]xyz"))
        self.assertEqual(False, supportsSSL("xyx[xyx]xyx"))
        self.assertEqual(True, supportsSSL("aaa[kek]eke"))
        self.assertEqual(True, supportsSSL("zazbz[bzb]cdb"))


if __name__ == '__main__':
    unittest.main()
