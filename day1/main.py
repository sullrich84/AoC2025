from math import ceil
from icecream import ic


def parseData(name="task"):
    lines = open(f"{name}.txt").read().splitlines()
    return lines


def solve1(data):
    pw = 0
    dial = 50
    for line in data:
        d = line[0]
        n = int(line[1:])

        if d == "L":
            dial -= n
        else:
            dial += n

        dial %= 100
        if dial == 0:
            pw += 1

    return pw


def solve2(data):
    pw = 0
    dial = 50
    for line in data:
        d = line[0]
        n = int(line[1:])

        nDial = dial
        step = -1 if d == "L" else 1

        for _ in range(n):
            nDial = (nDial + step) % 100
            if nDial == 0:
                pw += 1

        dial = nDial

    return pw


print("🎄 Day 1: Secret Entrance")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
