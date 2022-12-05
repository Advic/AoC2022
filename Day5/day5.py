# noinspection PyUnresolvedReferences
import re
from collections import OrderedDict

COMMAND_REGEX = r'move (?P<num>\d+) from (?P<source>\d+) to (?P<dest>\d+)'


class StackMover9000:

    def __init__(self, numstacks: int):
        self.stacks = OrderedDict()
        for i in range(numstacks):
            self.stacks[i + 1] = list()

    def move(self, num: int, source: int, dest: int):
        assert num > 0
        assert source > 0
        assert dest > 0
        assert dest != source
        for i in range(num):
            self.stacks[dest].append(self.stacks[source].pop())

    @property
    def tops(self) -> str:
        ret = ''
        for stack in self.stacks.values():
            ret += stack[-1]
        return ret


class StackMover9001(StackMover9000):
    def move(self, num: int, source: int, dest: int):
        assert num > 0
        assert source > 0
        assert dest > 0
        assert dest != source
        self.stacks[dest].extend(self.stacks[source][-num:])
        self.stacks[source] = self.stacks[source][:-num]


def part1(input: str) -> str:
    stackstr, commands = input.split('\n\n', 1)
    numstacks = int(re.findall('(\d+)', stackstr.rsplit('\n')[-1])[-1])
    stacks = StackMover9000(numstacks)

    for line in reversed(stackstr.split('\n')[:-1]):
        for stacknum in range(1, numstacks + 1):
            letterindex = 4 * (stacknum - 1) + 1
            try:
                crate = line[letterindex]
                if crate != ' ':
                    stacks.stacks[stacknum].append(crate)
            except IndexError:
                pass

    print(stacks.stacks)

    for command in commands.split('\n'):
        match = re.match(COMMAND_REGEX, command)
        stacks.move(*map(int, (match.group('num'), match.group('source'), match.group('dest'))))

    return stacks.tops


def part2(input: str) -> int:
    stackstr, commands = input.split('\n\n', 1)
    numstacks = int(re.findall('(\d+)', stackstr.rsplit('\n')[-1])[-1])
    stacks = StackMover9001(numstacks)

    for line in reversed(stackstr.split('\n')[:-1]):
        for stacknum in range(1, numstacks + 1):
            letterindex = 4 * (stacknum - 1) + 1
            try:
                crate = line[letterindex]
                if crate != ' ':
                    stacks.stacks[stacknum].append(crate)
            except IndexError:
                pass

    print(stacks.stacks)

    for command in commands.split('\n'):
        match = re.match(COMMAND_REGEX, command)
        stacks.move(*map(int, (match.group('num'), match.group('source'), match.group('dest'))))

    return stacks.tops


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
