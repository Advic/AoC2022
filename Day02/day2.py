# noinspection PyUnresolvedReferences
from enum import Enum


class WinScore(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6


class RockPaperScissors(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @property
    def winner(self):
        match self:
            case RockPaperScissors.ROCK:
                return RockPaperScissors.PAPER
            case RockPaperScissors.PAPER:
                return RockPaperScissors.SCISSORS
            case RockPaperScissors.SCISSORS:
                return RockPaperScissors.ROCK

    @property
    def loser(self):
        match self:
            case RockPaperScissors.ROCK:
                return RockPaperScissors.SCISSORS
            case RockPaperScissors.PAPER:
                return RockPaperScissors.ROCK
            case RockPaperScissors.SCISSORS:
                return RockPaperScissors.PAPER


player_map = {'X': RockPaperScissors.ROCK,
              'Y': RockPaperScissors.PAPER,
              'Z': RockPaperScissors.SCISSORS}

opponent_map = {'A': RockPaperScissors.ROCK,
                'B': RockPaperScissors.PAPER,
                'C': RockPaperScissors.SCISSORS}

strategy_map = {'X': WinScore.LOSS,
                'Y': WinScore.DRAW,
                'Z': WinScore.WIN}


def score_rounds(input: str) -> int:
    return sum(map(score_round, *zip(*[line.split(' ') for line in input.split('\n')])))


def score_round(opponent_str: str, player_str: str) -> int:
    assert opponent_str in opponent_map
    assert player_str in player_map

    return evaluate_win(opponent_map[opponent_str], player_map[player_str]).value + player_map[player_str].value


def evaluate_win(opponent: RockPaperScissors, player: RockPaperScissors) -> WinScore:
    if (opponent == player):
        return WinScore.DRAW
    elif ((player.value - opponent.value == 1) or (player.value - opponent.value == -2)):
        return WinScore.WIN
    else:
        return WinScore.LOSS


def score_rounds_p2(input: str) -> int:
    return sum(map(score_round_p2, *zip(*[line.split(' ') for line in input.split('\n')])))


def score_round_p2(opponent_str: str, strategy_str: str) -> int:
    assert opponent_str in opponent_map
    assert strategy_str in strategy_map
    strategy = strategy_map[strategy_str]
    player_pick = pick_strategy(opponent_map[opponent_str], strategy)
    return strategy.value + player_pick.value


def pick_strategy(opponent: RockPaperScissors, strategy: WinScore) -> RockPaperScissors:
    if (strategy == WinScore.DRAW):
        return opponent
    elif (strategy == WinScore.WIN):
        return opponent.winner
    else:
        return opponent.loser


if __name__ == '__main__':
    input = open('data.txt').read().strip()
    print("Result of func call is", score_rounds(input))
    print("Result of func call, part 2 is", score_rounds_p2(input))
