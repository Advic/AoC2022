import unittest

# noinspection PyUnresolvedReferences
from day3 import sumSackPriorities, sumBadgePriorities

TEST_DATA = open('test_data.txt').read()


class TestDay3(unittest.TestCase):

    def test_sumSackPriorities(self):
        self.assertEqual(sumSackPriorities(TEST_DATA), 157)

    def test_sumBadgePriorities(self):
        self.assertEqual(sumBadgePriorities(TEST_DATA), 70)


if __name__ == '__main__':
    unittest.main()
