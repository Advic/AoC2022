# noinspection PyUnresolvedReferences
from itertools import zip_longest


# https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


class Rucksack:
    def __init__(self, contents: str):
        self.contents = contents

    def findPriorityLetter(self) -> str:
        mid = int(len(self.contents) / 2)
        intersection = set(self.contents[:mid]).intersection(set(self.contents[mid:]))
        assert len(intersection) == 1
        return intersection.pop()

    @property
    def priority(self):
        letter = self.findPriorityLetter()
        return ord(letter) - 96 if letter.islower() else ord(letter) - 64 + 26


def sumSackPriorities(input: str) -> int:
    total = 0
    for line in input.splitlines():
        total += Rucksack(line).priority
    return total


def sumBadgePriorities(input: str) -> int:
    total = 0
    for group in grouper(input.splitlines(), 3):
        candidates = set(group[0])
        for sack in group[1:]:
            candidates.intersection_update(sack)
        assert len(candidates) == 1
        letter = candidates.pop()
        total += ord(letter) - 96 if letter.islower() else ord(letter) - 64 + 26
    return total


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", sumSackPriorities(input))
    print("Result of part 2 is", sumBadgePriorities(input))
