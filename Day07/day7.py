# noinspection PyUnresolvedReferences
import numpy as np


class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def prettyPrint(self, depth=0):
        return '  ' * depth + '- ' + self.name + f' (file, size={self.size})'


class Directory:
    def __init__(self, name: str):
        self.name = name
        self.files = dict()
        self.subdirectories = dict()

    def prettyPrint(self, depth=0):
        data = '  ' * depth + '- ' + self.name + ' (dir)'
        for subdir in self.subdirectories.values():
            data += '\n'
            data += subdir.prettyPrint(depth + 1)
        for file in self.files.values():
            data += '\n'
            data += file.prettyPrint(depth + 1)
        return data

    def filterSize(self, threshold=100000):
        s = sum([subdir.filterSize() for subdir in self.subdirectories.values()])
        if self.size <= threshold:
            s += self.size
        return s

    def listSizes(self):
        s = [self.size]
        # if self.subdirectories:
        for subdir in self.subdirectories.values():
            s.extend(subdir.listSizes())
        return s

    @property
    def size(self) -> int:
        return sum([file.size for file in self.files.values()]) + sum(
            [subdir.size for subdir in self.subdirectories.values()])


def part1(input: str, size: int = 100000) -> int:
    dirtree = parseCommands(input)
    return dirtree.filterSize(size)


def parseCommands(input: str) -> Directory:
    LS_OUTPUT_MODE = False

    ROOT_DIRECTORY = Directory('/')

    dirstack = list()
    curdir = None

    for line in input.splitlines():
        if line.startswith('$'):
            LS_OUTPUT_MODE = False
            # print(line[2:4])
            if line[2:4] == 'cd':
                if (line[5:] == '/'):
                    dirstack = [ROOT_DIRECTORY]
                    curdir = ROOT_DIRECTORY
                elif (line[5:] == '..'):
                    dirstack.pop()
                    curdir = dirstack[-1]
                else:
                    subdir = curdir.subdirectories[line[5:]]
                    dirstack.append(subdir)
                    curdir = subdir
                # print("CURRENT", curdir.name, [d.name for d in dirstack])
            elif line[2:4] == 'ls':
                LS_OUTPUT_MODE = True
            else:
                raise Exception(line)
        else:
            assert LS_OUTPUT_MODE
            if line.startswith('dir'):
                dirname = line[4:]
                if (dirname not in curdir.subdirectories):
                    curdir.subdirectories[dirname] = Directory(dirname)
            else:
                size, filename = line.split(' ', 1)
                if filename not in curdir.files:
                    curdir.files[filename] = File(filename, int(size))

    return ROOT_DIRECTORY


def part2(input: str, requiredSpace=30000000, totalSpace=70000000) -> int:
    dirtree = parseCommands(input)
    usedSpace = dirtree.size
    requiredDelete = usedSpace - (totalSpace - requiredSpace)
    # print("Used space:", usedSpace)
    # print("Required delete: ", requiredDelete)
    # print(sorted(dirtree.listSizes()))
    return next(val for val in sorted(dirtree.listSizes()) if val > requiredDelete)


if __name__ == '__main__':
    input = open('data.txt').read()
    print("Result of part 1 is", part1(input))
    print("Result of part 2 is", part2(input))
