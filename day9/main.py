from icecream import ic
from collections import defaultdict
from math import sqrt, prod
from heapq import heapify, heappop, heappush


def parseData(name="task"):
    return [
        (int(x[0]), int(x[1]))
        for x in [l.split(",") for l in open(f"{name}.txt").read().splitlines()]
    ]


def solve1(data):
    ans = 0
    for i, p1 in enumerate(data[:-1]):
        r1, c1 = p1
        for p2 in data[i + 1 :]:
            r2, c2 = p2
            h = abs(r2 - r1) + 1
            w = abs(c2 - c1) + 1
            area = h * w
            ans = max([ans, area])

    return ans


def solve2(data):
    def is_inside(p1, p2, poly):
        xmin, xmax = sorted([p1[0], p2[0]])
        ymin, ymax = sorted([p1[1], p2[1]])

        for i in range(len(poly)):
            x1, y1 = poly[i]
            x2, y2 = poly[(i + 1) % len(poly)]

            if y1 == y2:
                if ymin < y1 < ymax and (
                    min(x1, x2) <= xmin < max(x1, x2)
                    or min(x1, x2) < xmax <= max(x1, x2)
                ):
                    return False
            elif x1 == x2:
                if xmin < x1 < xmax and (
                    min(y1, y2) <= ymin < max(y1, y2)
                    or min(y1, y2) < ymax <= max(y1, y2)
                ):
                    return False

        return True

    ans = 0
    for i, p1 in enumerate(data[:-1]):
        for p2 in data[i + 1 :]:
            if is_inside(p1, p2, data):
                area = (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)
                ans = max(ans, area)

    return ans


print("🎄 Day 9: Movie Theater")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
