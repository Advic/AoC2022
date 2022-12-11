# noinspection PyUnresolvedReferences
import re
from math import prod
from operator import mul
from textwrap import dedent
from typing import Callable


class Monkey:
    MONKEY_REGEX = dedent("""\
        Monkey (?P<monkeyNum>.+):
          Starting items: (?P<startingItems>.+)
          Operation: new = (?P<term1>[0-9]+|old) (?P<operator>[+*]+) (?P<term2>[0-9]+|old)
          Test: divisible by (?P<test>\d+)
            If true: throw to monkey (?P<ifTrue>\d+)
            If false: throw to monkey (?P<ifFalse>\d+)""")

    @classmethod
    def parse(cls, chunk: str):
        match = re.match(Monkey.MONKEY_REGEX, chunk)
        monkeyNum = int(match.group('monkeyNum'))
        startingItems = list(map(int, match.group('startingItems').split(', ')))
        operation = lambda old: eval(match.group('term1') + match.group('operator') + match.group('term2'))
        test = int(match.group('test'))
        ifTrue = int(match.group('ifTrue'))
        ifFalse = int(match.group('ifFalse'))
        monkey = cls(monkeyNum, startingItems, operation, test, ifTrue, ifFalse)
        return monkey

    def __init__(self, monkeyNum: int,
                 startingItems: list[int],
                 operation: Callable[[int], int],
                 test: int,
                 ifTrue: int,
                 ifFalse: int):
        self.monkeyNum = monkeyNum
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.ifTrue = ifTrue
        self.ifFalse = ifFalse
        self.numInspection = 0

    def hasItems(self) -> bool:
        return bool(self.items)

    def inspect(self) -> (int, int):
        self.numInspection += 1
        item = self.items.pop(0)
        item = self.operation(item)
        item = int(item / 3)
        return (self.ifTrue, item) if item % self.test == 0 else (self.ifFalse, item)

    def receive(self, item):
        self.items.append(item)


class WorryingMonkeys(Monkey):
    def lcm(self, lcm):
        self.lcm = lcm

    def inspect(self) -> (int, int):
        self.numInspection += 1
        item = self.items.pop(0)
        item = self.operation(item)
        item = item % self.lcm
        return (self.ifTrue, item) if item % self.test == 0 else (self.ifFalse, item)


def part1(input: str) -> int:
    monkeys = list()
    for chunk in input.split('\n\n'):
        monkeys.append(Monkey.parse(chunk))
    for i in range(20):
        for monkey in monkeys:
            while monkey.hasItems():
                (target, item) = monkey.inspect()
                monkeys[target].receive(item)

    return mul(*list(sorted(monkey.numInspection for monkey in monkeys))[-2:])


def part2(input: str) -> int:
    monkeys = list()
    for chunk in input.split('\n\n'):
        monkeys.append(WorryingMonkeys.parse(chunk))

    # number theory: since our test condition is always performing modulo arithmetic, we can take the
    # item modulo the least common multiple of all the monkeys
    lcm = prod(monkey.test for monkey in monkeys)
    for monkey in monkeys:
        monkey.lcm(lcm)

    for i in range(10000):
        for monkey in monkeys:
            while monkey.hasItems():
                (target, item) = monkey.inspect()
                monkeys[target].receive(item)

    return mul(*list(sorted(monkey.numInspection for monkey in monkeys))[-2:])


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
