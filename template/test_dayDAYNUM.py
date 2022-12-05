import unittest

# noinspection PyUnresolvedReferences
from dayDAYNUM import *

TEST_DATA = open('test_data.txt').read()

PART1_EXPECTED = None
PART2_EXPECTED = None


class TestDayDAYNUM(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(PART1_EXPECTED, part1(TEST_DATA))

    def test_part2(self):
        self.assertEqual(PART2_EXPECTED, part2(TEST_DATA))


if __name__ == '__main__':
    unittest.main()
