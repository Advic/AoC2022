# noinspection PyUnresolvedReferences
from __future__ import annotations

import re

SENSOR_RE = r'Sensor at x=(?P<sensorx>[\d-]+), y=(?P<sensory>[\d-]+): closest beacon is at x=(?P<beaconx>[\d-]+), y=(?P<beacony>[\d-]+)'


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, other: this):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def getPointsWithinRadius(self, r: int) -> set[tuple[int, int]]:
        ret = set()
        for i in range(- r, r + 1):
            for j in range(-abs(r - abs(i)), abs(r - abs(i)) + 1):
                ret.add((self.x + i, self.y + j))
        return ret


class Sensor:
    def __init__(self, position: Coordinate, beacon: Coordinate):
        self.pos = position
        # self.beacon = beacon
        self.distance = position.distance(beacon)

    def closestBeaconIsCloserThan(self, coord: Coordinate) -> bool:
        return self.distance < self.pos.distance(coord)


def part1(input: str, deadzoney) -> int:
    # impossiblePositions = set()
    beacons = set()
    sensors = list()
    sensors_hashable = set()

    for line in input.splitlines():
        match = re.match(SENSOR_RE, line)
        sensor = Coordinate(int(match.group('sensorx')), int(match.group('sensory')))
        beacon = Coordinate(int(match.group('beaconx')), int(match.group('beacony')))
        sensors.append(Sensor(sensor, beacon))
        beacons.add((beacon.x, beacon.y))
        sensors_hashable.add((sensor.x, sensor.y))
        # d = sensor.distance(beacon)
        # list(map(impossiblePositions.add, sensor.getPointsWithinRadius(d)))
        # print("Processed a line")

    ranges = list()
    for sensor in sorted(sensors, key=lambda s: s.pos.x):
        if (sensor.distance > abs(deadzoney - sensor.pos.y)):
            ranges.append((sensor.pos.x - abs(sensor.distance - abs(deadzoney - sensor.pos.y)),
                           sensor.pos.x + abs(sensor.distance - abs(deadzoney - sensor.pos.y))))

    print(ranges)
    total = 0
    highest_counted = float('-inf')
    for (rangestart, rangeend) in ranges:
        if rangestart > highest_counted:
            print("Add " + str(rangeend - rangestart + 1) + ", rangeend " + str(rangeend) + " rangestart " + str(rangestart))
            total += rangeend - rangestart + 1
            highest_counted = rangeend
        elif rangeend > highest_counted:
            print("Add " + str(rangeend - highest_counted) + " rangeend " + str(rangeend) + " highest_counted " + str(highest_counted))
            total += rangeend - highest_counted
            highest_counted = rangeend

    # sortedBeacons = list(sorted(list(beacons) + list(sensors_hashable), key=lambda thing: thing[0]))
    # total = 0
    # for x in range(sortedBeacons[0][0], sortedBeacons[-1][0] + 1):
    #     coord = Coordinate(x, deadzoney)
    #     if any(map(lambda s: not s.closestBeaconIsCloserThan(coord), sensors)) and (coord.x, coord.y) not in beacons:
    #         total += 1
    #
    # print("Checking right side")
    # x = sortedBeacons[-1][0] + 1
    # coord = Coordinate(x, deadzoney)
    # impossible = (coord.x, coord.y) not in beacons and any(
    #     map(lambda s: not s.closestBeaconIsCloserThan(coord), sensors))
    # while impossible:
    #     total += 1
    #     x += 1
    #     impossible = any(map(lambda s: not s.closestBeaconIsCloserThan(coord), sensors)) and (coord.x, coord.y) not in beacons
    #
    # print("Checking left side")
    # x = sortedBeacons[0][0] - 1
    # coord = Coordinate(x, deadzoney)
    # impossible = any(map(lambda s: not s.closestBeaconIsCloserThan(coord), sensors)) and (coord.x, coord.y) not in beacons
    # while impossible:
    #     total += 1
    #     x -= 1
    #     impossible = any(map(lambda s: not s.closestBeaconIsCloserThan(coord), sensors)) and (coord.x, coord.y) not in beacons

    # impossiblePositions -= beaconLocations
    # print(impossiblePositions)
    for beacon in beacons:
        if beacon[1] == deadzoney:
            total -= 1

    return total


def part2(input: str) -> int:
    total = 0
    for line in input.splitlines():
        pass
    return total


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input, deadzoney=2000000))
    print("Result of part 2 is", part2(input))
