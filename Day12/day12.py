# noinspection PyUnresolvedReferences
import numpy as np


def parse_heightmap(input: str, padval: int = 100) -> np.array:
    arr = list()
    for line in input.splitlines():
        row = list()
        for char in line:
            if char == 'S':
                row.append(0)
            elif char == 'E':
                row.append(27)
            else:
                row.append(ord(char) - 96)
        arr.append(row)

    heightmap = np.array(arr)
    # pad to make things nicer later
    # if padval:
    heightmap = np.pad(heightmap, 1, mode='constant', constant_values=(padval,))

    start = np.where(heightmap == 0)
    end = np.where(heightmap == 27)
    heightmap[start] = 1

    heightmap[end] = 26

    return heightmap, start, end


def part1(input: str) -> int:
    heights, start, finish = parse_heightmap(input, padval=100)
    mindistance = np.ones(heights.shape) * -1
    mindistance[start] = 0

    searchdepth = 1
    while (mindistance[finish] == -1 and searchdepth < 1000):
        boundary = np.where(mindistance == searchdepth - 1)
        for x, y in zip(*boundary):
            for candidate in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if (mindistance[candidate] == -1) and (heights[candidate] <= heights[x, y] + 1):
                    mindistance[candidate] = searchdepth

        searchdepth += 1
    return int(mindistance[finish][0])


def part2(input: str) -> int:
    heights, start, finish = parse_heightmap(input, padval=-100)
    mindistance = np.ones(heights.shape) * -1
    mindistance[finish] = 0
    heights = -heights

    searchdepth = 1
    avalues = np.where(heights == -1)
    while ((mindistance[avalues] == -1).all() and searchdepth < 1000):
        boundary = np.where(mindistance == searchdepth - 1)
        for x, y in zip(*boundary):
            for candidate in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if (mindistance[candidate] == -1) and (heights[candidate] <= heights[x, y] + 1):
                    mindistance[candidate] = searchdepth

        searchdepth += 1

    return int(mindistance[avalues].max())


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
