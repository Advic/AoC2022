# noinspection PyUnresolvedReferences
import numpy as np


def part1(input: str) -> int:
    seenPlaces = set()
    head = np.array([0, 0])
    tail = np.array([0, 0])
    for line in input.splitlines():
        direction, distance = line.split()
        distance = int(distance)

        for step in range(distance):

            match direction:
                case "L":
                    head += np.array([-1, 0])
                case "R":
                    head += np.array([1, 0])
                case "U":
                    head += np.array([0, 1])
                case "D":
                    head += np.array([0, -1])
            separation = head - tail
            if (np.abs(separation) > np.array([1, 1])).any():
                motion = (np.abs(separation) - np.array((np.abs(separation) - np.array((1, 1))) > 0)) * np.sign(
                    separation)
                tail += motion

            # print("Head pos", head)
            # print("Tail pos", tail)
            # print()
            seenPlaces.add((tail[0], tail[1]))

    return len(seenPlaces)


def part2(input: str, ropelength=10) -> int:
    seenPlaces = set()
    # head = np.array([0, 0])
    # tail = np.array([0, 0])
    rope = [np.array([0, 0]) for i in range(ropelength)]
    for line in input.splitlines():
        direction, distance = line.split()
        distance = int(distance)

        for step in range(distance):

            match direction:
                case "L":
                    rope[0] += np.array([-1, 0])
                case "R":
                    rope[0] += np.array([1, 0])
                case "U":
                    rope[0] += np.array([0, 1])
                case "D":
                    rope[0] += np.array([0, -1])
            for lead, follow in zip(rope[:-1], rope[1:]):
                separation = lead - follow
                if (np.abs(separation) > np.array([1, 1])).any():
                    motion = (np.abs(separation) - np.array((np.abs(separation) - np.array((1, 1))) > 0)) * np.sign(
                        separation)
                    follow += motion

            tail = rope[-1]
            seenPlaces.add((tail[0], tail[1]))

    return len(seenPlaces)


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
