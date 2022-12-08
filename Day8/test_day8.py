import unittest

# noinspection PyUnresolvedReferences
from day8 import *

TEST_DATA = open('test_data.txt').read()
TEST_DATA_ARR = np.array([list(iter(line)) for line in TEST_DATA.splitlines()])

PART1_EXPECTED = 21
PART2_EXPECTED = 4


class TestDay8(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(PART1_EXPECTED, part1(TEST_DATA))

    def test_part2(self):
        self.assertEqual(PART2_EXPECTED, calculateScenicScore(TEST_DATA_ARR, (1, 2)))

if __name__ == '__main__':
    unittest.main()
