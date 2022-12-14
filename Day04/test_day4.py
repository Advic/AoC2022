import unittest

# noinspection PyUnresolvedReferences
from day4 import *

TEST_DATA = open('test_data.txt').read()


class TestDay4(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(2, part1(TEST_DATA))

    def test_part2(self):
        self.assertEqual(4, part2(TEST_DATA))


if __name__ == '__main__':
    unittest.main()
