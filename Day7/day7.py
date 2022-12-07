# noinspection PyUnresolvedReferences
import re

ABBA_REGEX = r'((\w)(\w)\3\2)'
ABA_REGEX = r'(\w)(?=\w\1)'


def part1(input: str) -> int:
    total = 0
    for line in input.splitlines():
        i = supportsTLS(line)
        if i:
            total += 1
    return total


def supportsTLS(input: str) -> int:
    match = re.search(ABBA_REGEX, input)
    if match is None:
        return False
    for start, stop in match.regs[1::3]:
        if input[:start].count(']') != input[:start].count('['):
            return False
        if input[start] == input[start + 1]:
            return False
    return match.regs[0][0]


def part2(input: str) -> int:
    total = 0
    for line in input.splitlines():
        if (supportsSSL(line)):
            total += 1
    return total


def supportsSSL(input: str) -> int:
    abas = re.finditer(ABA_REGEX, input)
    if abas is None:
        return False

    abamap = set()
    babmap = set()

    for match in abas:
        start = match.regs[0][0]
        if input[start] == input[start + 1]:
            continue
        # print(start)

        if input[:start].count(']') != input[:start].count('['):
            abamap.add(input[start] + input[start + 1])
        else:
            babmap.add(input[start] + input[start + 1])

    print(abamap, babmap)
    for aba in abamap:
        if aba[::-1] in babmap:
            return True
    return False


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
