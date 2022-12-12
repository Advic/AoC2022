import unittest

# noinspection PyUnresolvedReferences
from day12 import *

TEST_DATA = open('test_data.txt').read()

PART1_EXPECTED = 31
PART2_EXPECTED = 29


class TestDay12(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(PART1_EXPECTED, part1(TEST_DATA))

    def test_part2(self):
        self.assertEqual(PART2_EXPECTED, part2(TEST_DATA))


if __name__ == '__main__':
    unittest.main()
