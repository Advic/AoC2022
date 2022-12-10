# noinspection PyUnresolvedReferences
import textwrap

import numpy as np


def part1(input: str) -> int:
    signal = [0]
    currentStrength = 1
    signal.append(currentStrength)
    for line in input.splitlines():
        if line.startswith("noop"):
            signal.append(currentStrength)
        elif line.startswith("addx"):
            signal.append(currentStrength)
            currentStrength += int(line.split(" ", 1)[1])
            signal.append(currentStrength)
        else:
            assert False
    return sum([a * b for a, b in enumerate(signal)][20::40])


CRT_WIDTH = 40
CRT_HEIGHT = 6


def part2(input: str, datachar='#', blankchar=' ') -> str:
    signal = [0]
    currentStrength = 1
    ret = str()
    signal.append(currentStrength)
    for line in input.splitlines():
        if line.startswith("noop"):
            signal.append(currentStrength)
        elif line.startswith("addx"):
            signal.append(currentStrength)
            currentStrength += int(line.split(" ", 1)[1])
            signal.append(currentStrength)
        else:
            assert False

    for cyclenum, strength in enumerate(signal[1:]):
        if abs(cyclenum % CRT_WIDTH - strength) <= 1:
            ret += datachar
        else:
            ret += blankchar

    return '\n'.join(textwrap.wrap(ret[:CRT_WIDTH * CRT_HEIGHT], CRT_WIDTH))


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is\n", part2(input))
