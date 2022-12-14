import unittest

# noinspection PyUnresolvedReferences
from day6 import *

TEST_DATA = open('test_data.txt').read()

PART1_EXPECTED = 7
PART2_EXPECTED = 19


class TestDay6(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(PART1_EXPECTED, part1(TEST_DATA))

    def test_part2(self):
        self.assertEqual(PART2_EXPECTED, part2(TEST_DATA))


if __name__ == '__main__':
    unittest.main()
