from icecream import ic
from math import sqrt, prod
from functools import cache
from heapq import heapify, heappop, heappush
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, cycle, product


def parseData(name="task"):
    rows = []
    file = [l.split(" ") for l in open(f"{name}.txt").read().splitlines()]
    for line in file:
        row = []
        for i, pack in enumerate(line):
            p = pack[1:-1]
            if i == 0:
                p = [1 if i == "#" else 0 for i in list(p)]
            if i > 0:
                p = [int(i) for i in p.split(",")]
            row.append(p)
        rows.append(row)
    return rows


def solve1(rows):
    ans = 0
    for row in rows:
        target = sum(1 << i for i, v in enumerate(row[0]) if v == 1)

        masks = []
        for btn in row[1:-1]:
            masks.append(sum(1 << b for b in btn))

        min_presses = float("inf")
        for presses in product([0, 1], repeat=len(masks)):
            state = 0
            for i, press in enumerate(presses):
                if press:
                    state ^= masks[i]
            if state == target:
                min_presses = min(min_presses, sum(presses))
        ans += min_presses
    return ans


def solve2(rows):
    ans = 0
    for row in rows:
        masks = row[1:-1]
        jolts = row[-1]

        @cache
        def dp(idx, remaining):
            if idx == len(masks):
                return 0 if all(r == 0 for r in remaining) else float("inf")

            min_p = float("inf")
            max_presses = max((remaining[j] for j in masks[idx]), default=0)

            for presses in range(max_presses + 1):
                new_rem = list(remaining)
                for j in masks[idx]:
                    new_rem[j] -= presses

                cost = presses + dp(idx + 1, tuple(new_rem))
                min_p = min(min_p, cost)

            return min_p

        min_presses = dp(0, tuple(jolts))
        ans += min_presses
    return ans


print("🎄 Day 10: XXX")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
