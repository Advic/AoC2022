import unittest

# noinspection PyUnresolvedReferences
from day2 import *

TEST_DATA = open('test_data.txt').read()


class TestDay2(unittest.TestCase):
    def test_win(self):
        self.assertEqual(evaluate_win(RockPaperScissors.PAPER, RockPaperScissors.SCISSORS), WinScore.WIN)
        self.assertEqual(evaluate_win(RockPaperScissors.SCISSORS, RockPaperScissors.ROCK), WinScore.WIN)
        self.assertEqual(evaluate_win(RockPaperScissors.ROCK, RockPaperScissors.PAPER), WinScore.WIN)

        self.assertEqual(evaluate_win(RockPaperScissors.SCISSORS, RockPaperScissors.PAPER), WinScore.LOSS)
        self.assertEqual(evaluate_win(RockPaperScissors.ROCK, RockPaperScissors.SCISSORS), WinScore.LOSS)
        self.assertEqual(evaluate_win(RockPaperScissors.PAPER, RockPaperScissors.ROCK), WinScore.LOSS)

        self.assertEqual(evaluate_win(RockPaperScissors.ROCK, RockPaperScissors.ROCK), WinScore.DRAW)
        self.assertEqual(evaluate_win(RockPaperScissors.PAPER, RockPaperScissors.PAPER), WinScore.DRAW)
        self.assertEqual(evaluate_win(RockPaperScissors.SCISSORS, RockPaperScissors.SCISSORS), WinScore.DRAW)

    def test_score_round(self):
        self.assertEqual(score_rounds(TEST_DATA), 15)

    def test_score_round_part2(self):
        self.assertEqual(score_rounds_p2(TEST_DATA), 12)


if __name__ == '__main__':
    unittest.main()
