# noinspection PyUnresolvedReferences
import numpy as np


def part1(input: str) -> int:
    count = 0
    for line in input.splitlines():
        elf1, elf2 = line.split(',', 1)
        elf1l, elf1r = map(int, elf1.split('-', 1))
        elf2l, elf2r = map(int, elf2.split('-', 1))
        if eithercontains(set(range(elf1l, elf1r + 1)), set(range(elf2l, elf2r + 1))):
            count += 1
    return count


def eithercontains(range1: set, range2: set) -> bool:
    return range1.issubset(range2) or range2.issubset(range1)


def part2(input: str) -> int:
    count = 0
    for line in input.splitlines():
        elf1, elf2 = line.split(',', 1)
        elf1l, elf1r = map(int, elf1.split('-', 1))
        elf2l, elf2r = map(int, elf2.split('-', 1))
        if anyoverlap(set(range(elf1l, elf1r + 1)), set(range(elf2l, elf2r + 1))):
            count += 1
    return count


def anyoverlap(range1: set, range2: set) -> bool:
    return not range1.isdisjoint(range2)


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
