import textwrap
import unittest

# noinspection PyUnresolvedReferences
from day10 import *

TEST_DATA = open('test_data.txt').read()

PART1_EXPECTED = 13140
PART2_EXPECTED = textwrap.dedent("""\
    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....""")


class TestDay10(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(PART1_EXPECTED, part1(TEST_DATA))

    def test_part2(self):
        print(part2(TEST_DATA))
        self.assertEqual(PART2_EXPECTED, part2(TEST_DATA, blankchar='.'))


if __name__ == '__main__':
    unittest.main()
