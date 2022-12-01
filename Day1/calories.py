def calories(txt: str, numtop: int = 1) -> int:
    assert numtop >= 1
    elfnum = 0
    caloriemap = {0: 0}
    for line in txt.split('\n'):
        if not line:
            elfnum += 1
            caloriemap[elfnum] = 0
        else:
            caloriemap[elfnum] += int(line)
    return sum(sorted(caloriemap.values())[-numtop:])


if __name__ == '__main__':
    arr = open('data.txt').read()
    print("Top elf:", calories(arr))
    print("Top 3 elves:", calories(arr, 3))
