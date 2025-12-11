from functools import cache
from heapq import heapify, heappop, heappush
from collections import defaultdict


def parseData(name="task"):
    servers = defaultdict(list)
    for line in open(f"{name}.txt").read().splitlines():
        node, adj = line.split(": ")
        servers[node] = adj.split(" ")
    return servers


def solve1(servers):
    stack = [(0, [], "you")]
    heapify(stack)

    paths = list()
    while stack:
        steps, path, cur = heappop(stack)
        npath = path + [cur]

        if cur == "out":
            paths.append(npath)
            continue

        for out in servers[cur]:
            nsteps = steps + 1
            heappush(stack, (nsteps, npath, out))

    return len(paths)


def solve2(servers):
    @cache
    def count_paths(start, end):
        if start == end:
            return 1
        return sum(count_paths(srv, end) for srv in servers[start])

    via_dac = (
        count_paths("svr", "dac")
        * count_paths("dac", "fft")
        * count_paths("fft", "out")
    )
    via_fft = (
        count_paths("svr", "fft")
        * count_paths("fft", "dac")
        * count_paths("dac", "out")
    )

    return via_dac + via_fft


print("🎄 Day 11: Reactor")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("sample")))
