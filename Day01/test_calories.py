import unittest
from textwrap import dedent

from calories import calories

TEST_DATA = dedent("""\
    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000""")


class TestCalories(unittest.TestCase):
    def test_getcalories(self):
        self.assertEqual(24000, calories(TEST_DATA))

    def test_getcalories_topthree(self):
        self.assertEqual(45000, calories(TEST_DATA, 3))


if __name__ == '__main__':
    unittest.main()
