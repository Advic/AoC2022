# noinspection PyUnresolvedReferences
from enum import Enum

import numpy as np
from PIL import Image

SAND_SOURCE = (500, 0)

ARR_SIZE = (1000, 1000)

EMPTY = 0
WALL = 1
SAND = 2


def part1(input: str) -> int:
    arr = np.zeros(ARR_SIZE) * EMPTY
    for line in input.splitlines():
        points = list(map(lambda point: list(map(int, point.split(','))), line.split(' -> ')))
        for (wallstart, wallend) in zip(points[:-1], points[1:]):
            arr[wallstart[0], wallstart[1]] = WALL
            arr[wallend[0], wallend[1]] = WALL
            if wallstart[0] == wallend[0]:
                for i in range(*sorted((wallstart[1], wallend[1]))):
                    arr[wallstart[0], i] = WALL
            elif wallstart[1] == wallend[1]:
                for i in range(*sorted((wallstart[0], wallend[0]))):
                    arr[i, wallstart[1]] = WALL
            else:
                assert False

    while True:
        try:
            unit = list(SAND_SOURCE)
            done = False
            while not done:
                if arr[unit[0], unit[1] + 1] == EMPTY:
                    unit[1] += 1
                elif arr[unit[0] - 1, unit[1] + 1] == EMPTY:
                    unit[0] -= 1
                    unit[1] += 1
                elif arr[unit[0] + 1, unit[1] + 1] == EMPTY:
                    unit[0] += 1
                    unit[1] += 1
                else:
                    done = True
            arr[unit[0], unit[1]] = SAND
        except IndexError:
            break

    # arr[490:510, 0:20].T
    # display_sandarray(arr, 'part1.png')
    return np.count_nonzero(arr == SAND)


def part2(input: str) -> int:
    arr = np.zeros(ARR_SIZE) * EMPTY
    for line in input.splitlines():
        points = list(map(lambda point: list(map(int, point.split(','))), line.split(' -> ')))
        for (wallstart, wallend) in zip(points[:-1], points[1:]):
            arr[wallstart[0], wallstart[1]] = WALL
            arr[wallend[0], wallend[1]] = WALL
            if wallstart[0] == wallend[0]:
                for i in range(*sorted((wallstart[1], wallend[1]))):
                    arr[wallstart[0], i] = WALL
            elif wallstart[1] == wallend[1]:
                for i in range(*sorted((wallstart[0], wallend[0]))):
                    arr[i, wallstart[1]] = WALL
            else:
                assert False

    arr[:, np.where(arr == WALL)[1].max() + 2] = WALL

    while arr[SAND_SOURCE] == EMPTY:
        try:
            unit = list(SAND_SOURCE)
            done = False
            while not done:
                if arr[unit[0], unit[1] + 1] == EMPTY:
                    unit[1] += 1
                elif arr[unit[0] - 1, unit[1] + 1] == EMPTY:
                    unit[0] -= 1
                    unit[1] += 1
                elif arr[unit[0] + 1, unit[1] + 1] == EMPTY:
                    unit[0] += 1
                    unit[1] += 1
                else:
                    done = True
            arr[unit[0], unit[1]] = SAND
        except IndexError:
            break

    # arr[490:510, 0:20].T
    # display_sandarray(arr, 'part2.png')
    return np.count_nonzero(arr == SAND)


def display_sandarray(arr: np.array, filename: str):
    img = Image.new('RGB', ARR_SIZE, 'white')  # Create a new black image
    pixels = img.load()  # Create the pixel map
    for x, y in zip(*np.where(arr == SAND)):
        pixels[x, y] = (194, 178, 128)
    for x, y in zip(*np.where(arr == WALL)):
        pixels[x, y] = (100, 100, 100)
    # img.show()
    img.save(filename)


if __name__ == '__main__':
    input = open('data.txt').read()
    print('Result of part 1 is', part1(input))
    print('Result of part 2 is', part2(input))
