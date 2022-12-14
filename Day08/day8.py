# noinspection PyUnresolvedReferences
import numpy as np


def part1(input: str) -> int:
    total = 0
    arr = np.array([list(iter(line)) for line in input.splitlines()])
    for idx, val in np.ndenumerate(arr):
        x, y = idx
        if ((val > arr[:x, y]).all() or
            (val > arr[x + 1:, y]).all() or
            (val > arr[x, y + 1:]).all() or
            (val > arr[x, :y])).all():
            total += 1
    return total


def part2(input: str) -> int:
    highestScore = 0
    arr = np.array([list(iter(line)) for line in input.splitlines()])
    for idx, val in np.ndenumerate(arr):
        highestScore = max(highestScore, calculateScenicScore(arr, idx))
    return highestScore


def calculateScenicScore(arr: np.ndarray, idx: tuple) -> int:
    topscore = 0
    bottomscore = 0
    leftscore = 0
    rightscore = 0

    val = arr[idx]

    x, y = idx
    x -= 1
    while (x >= 0 and val > arr[x, y]):
        x -= 1
        topscore += 1
    if (x >= 0 and val == arr[x, y]):
        topscore += 1

    x, y = idx
    x += 1
    while (x < arr.shape[0] and val > arr[x, y]):
        x += 1
        bottomscore += 1
    if (x < arr.shape[0] and val == arr[x, y]):
        bottomscore += 1

    x, y = idx
    y -= 1
    while (y >= 0 and val > arr[x, y]):
        y -= 1
        leftscore += 1
    if (y >= 0 and val == arr[x, y]):
        leftscore += 1

    x, y = idx
    y += 1
    while (y < arr.shape[1] and val > arr[x, y]):
        y += 1
        rightscore += 1
    if (y < arr.shape[1] and val == arr[x, y]):
        rightscore += 1

    return topscore * bottomscore * leftscore * rightscore


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
