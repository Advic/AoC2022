# noinspection PyUnresolvedReferences
from functools import cmp_to_key


def part1(input: str) -> int:
    total = 0
    for i, chunk in enumerate(input.split('\n\n'), 1):
        line1, line2 = chunk.split('\n')
        left = eval(line1)
        right = eval(line2)
        if cmp(left, right) == -1:
            total += i
    return total


def listify(x) -> list:
    return x if isinstance(x, list) else [x]


def cmp(l: list, r: list) -> int:
    if isinstance(l, int) and isinstance(r, int):
        if (l < r):
            return -1
        elif (l > r):
            return 1
        else:
            return 0
    elif isinstance(l, list) and isinstance(r, list):
        for ret in map(cmp, l, r):
            if ret != 0:
                return ret
        if len(l) < len(r):
            return -1
        elif len(l) > len(r):
            return 1
        else:
            return 0
    else:
        return cmp(listify(l), listify(r))


def part2(input: str) -> int:
    data = list()
    for line in input.splitlines():
        if not line:
            continue
        data.append(eval(line))

    v1 = [[2]]
    v2 = [[6]]

    data.append(v1)
    data.append(v2)

    data.sort(key=cmp_to_key(cmp))
    return (data.index(v1) + 1) * (data.index(v2) + 1)


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
