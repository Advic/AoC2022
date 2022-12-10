import unittest

# noinspection PyUnresolvedReferences
from day9 import *

TEST_DATA = open('test_data.txt').read()
TEST_DATA2 = open('test_data2.txt').read()

PART1_EXPECTED = 13
PART2_EXPECTED = 36


class TestDay9(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(PART1_EXPECTED, part1(TEST_DATA))

    def test_part2(self):
        self.assertEqual(PART2_EXPECTED, part2(TEST_DATA2))


if __name__ == '__main__':
    unittest.main()
