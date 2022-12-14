import unittest

from lcm import lcm, getPrimeFactors


class TestLcm(unittest.TestCase):
    def test_getlcm(self):
        self.assertEqual(lcm([2, 2]), 2)
        self.assertEqual(lcm([2, 3]), 6)
        self.assertEqual(lcm([2, 6]), 6)
        self.assertEqual(lcm([12, 8]), 24)

    def test_getfactors(self):
        self.assertEqual(getPrimeFactors(2), {2: 1})
        self.assertEqual(getPrimeFactors(20), {2: 2, 5: 1})
        self.assertEqual(getPrimeFactors(84), {2: 2, 3: 1, 7: 1})
        self.assertEqual(getPrimeFactors(100), {2: 2, 5: 2})


if __name__ == '__main__':
    unittest.main()
