from icecream import ic
from math import sqrt, prod
import heapq


def parseData(name="task"):
    data = [l.split(",") for l in open(f"{name}.txt").read().splitlines()]
    space = []
    for x, y, z in data:
        space.append((int(x), int(y), int(z)))
    return space


def merge(data):
    merged = []
    for s in data:
        s = set(s)
        changed = True
        while changed:
            changed = False
            for m in merged[:]:
                if not s.isdisjoint(m):
                    s |= m
                    merged.remove(m)
                    changed = True
        merged.append(s)
    return merged


def solve1(data):
    distances = []
    heapq.heapify(distances)

    for i, a in enumerate(data):
        for b in data[i + 1 :]:
            d = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)
            heapq.heappush(distances, (d, a, b))

    circuits = []
    for _ in range(1000):
        m = heapq.heappop(distances)
        d, a, b = m

        added_to_circ = False
        for circ in circuits:
            if a in circ or b in circ:
                circ.update([a, b])
                added_to_circ = True
                # print("--> ADDED TO EXISTING CIRCUITE")
        if not added_to_circ:
            circuits.append(set([a, b]))
            # print("--> NEW CIRCUITE")

    merged = merge(circuits)
    lens = sorted([len(s) for s in merged], reverse=True)
    return prod(lens[0:3])


def solve2(data):
    return 0


print("🎄 Day 8: XXX")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("sample")))
