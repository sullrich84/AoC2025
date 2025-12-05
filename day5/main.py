def parseData(name="task"):
    data = open(f"{name}.txt").read().splitlines()
    ranges = sorted([tuple(map(int, r.split("-"))) for r in data[: data.index("")]])
    ingred = [int(r) for r in data[data.index("") + 1 :]]
    return (ranges, ingred)


def solve1(data):
    ranges, ingred = data
    fresh = set()
    for i in ingred:
        for mi, mx in ranges:
            if i >= mi and i <= mx:
                fresh.add(i)

    return len(fresh)


def solve2(data):
    ranges, _ = data
    stack = sorted(ranges)
    changed = True
    while changed:
        changed = False
        new_stack = []

        prev = stack[0]
        for curr in stack[1:]:
            if curr[0] <= prev[1] + 1:
                prev = (prev[0], max(prev[1], curr[1]))
                changed = True
            else:
                new_stack.append(prev)
                prev = curr

        new_stack.append(prev)
        stack = sorted(new_stack)

    return sum([s[1] - s[0] + 1 for s in stack])


print("🎄 Day 5: Cafeteria")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
