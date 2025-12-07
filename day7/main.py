from icecream import ic
from collections import defaultdict


def parseData(name="task"):
    file = open(f"{name}.txt").read().splitlines()
    grid, start = (list(), None)
    for row in range(len(file)):
        for col in range(len(file[0])):
            if file[row][col] == "^":
                grid.append((row, col))
            elif file[row][col] == "S":
                start = (row, col)
    rmax = max([p[0] for p in grid])
    return (grid, start, rmax)


def solve1(data):
    grid, start, rmax = data
    active = set([start[1]])
    splits = 0

    for r in range(1, rmax + 1):
        splitter = set([p[1] for p in grid if p[0] == r])
        collisions = active & splitter
        splits += len(collisions)

        for coll in collisions:
            active.remove(coll)
            active.add(coll - 1)
            active.add(coll + 1)

    return splits


def solve2(data):
    grid, start, rmax = data
    active = defaultdict(int)
    active[start[1]] = 1

    for r in range(1, rmax + 1):
        splitter = set([p[1] for p in grid if p[0] == r])
        nactive = defaultdict(int)

        for c, beams in active.items():
            if c not in splitter:
                # Create a new timeline
                nactive[c] += beams

        for coll in active.keys() & splitter:
            # Create two new timelines for each collision
            nactive[coll - 1] += active[coll]
            nactive[coll + 1] += active[coll]

        active = nactive

    return sum(active.values())


print("🎄 Day 7: Laboratories")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
