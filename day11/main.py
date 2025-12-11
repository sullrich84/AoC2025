from icecream import ic
from math import sqrt, prod
from functools import cache
from heapq import heapify, heappop, heappush
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, cycle


def parseData(name="task"):
    file = [
        l.replace(":", "").split(" ") for l in open(f"{name}.txt").read().splitlines()
    ]
    return {s[0]: s[1:] for s in file}


def solve1(servers, start, end):
    stack = [(0, [], start)]

    heapify(stack)
    paths = list()
    seen = set()

    while stack:
        steps, path, cur = heappop(stack)
        npath = path + [cur]

        key = ",".join(npath)
        if key in seen:
            continue
        seen.add(key)

        if cur == end:
            paths.append(npath)
            continue

        if cur not in servers:
            continue

        for out in servers[cur]:
            if out in npath:
                continue
            nsteps = steps + 1
            heappush(stack, (nsteps, npath, out))

    return paths


def solve2(data):
    ans = 0

    path1 = solve1(data, "svr", "fft")
    ic(len(path1))
    path2 = solve1(data, "fft", "dac")
    ic(len(path2))

    ic(path1, path2)
    return len(path1) + len(path2)


print("🎄 Day 11: XXX")
print("Part 1:", len(solve1(parseData("task"), "you", "out")))
print("Part 2:", solve2(parseData("sample")))
