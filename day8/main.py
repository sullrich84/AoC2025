from icecream import ic
from math import sqrt, prod
from heapq import heapify, heappop, heappush


def parseData(name="task"):
    data = [l.split(",") for l in open(f"{name}.txt").read().splitlines()]
    space = []
    for x, y, z in data:
        space.append((int(x), int(y), int(z)))
    return space


def calc_distances(data):
    distances = []
    heapify(distances)
    for i, a in enumerate(data):
        for b in data[i + 1 :]:
            d = sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2 + (b[2] - a[2]) ** 2)
            heappush(distances, (d, a, b))
    return distances


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
    distances = calc_distances(data)
    circuits = []
    for _ in range(10):
        p = heappop(distances)
        _, px, py = p

        added_to_circ = False
        for circ in circuits:
            if px in circ or py in circ:
                circ.update([px, py])
                added_to_circ = True
        if not added_to_circ:
            circuits.append(set([px, py]))

    merged = merge(circuits)
    lens = sorted([len(s) for s in merged], reverse=True)
    return prod(lens[0:3])


def solve2(data):
    distances = calc_distances(data)
    parent = {box: box for box in data}
    ic(parent)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py
            return True
        return False

    last_connection = None
    while distances:
        _, a, b = heappop(distances)

        if union(a, b):
            last_connection = (a, b)

            root = find(data[0])
            if all(find(box) == root for box in data):
                break

    if last_connection:
        return last_connection[0][0] * last_connection[1][0]
    return 0


print("🎄 Day 8: Playground")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
