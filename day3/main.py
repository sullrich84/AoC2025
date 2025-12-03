def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def joltage(line, size):
    nums = list(line)
    length = len(nums)
    res = list()
    start = 0

    for i in reversed(range(size)):
        remaining = nums[start : length - i]
        res.append(max(remaining))
        start += remaining.index(res[-1]) + 1

    return int("".join(res))


def solve1(data):
    return sum([joltage(x, 2) for x in data])


def solve2(data):
    return sum([joltage(x, 12) for x in data])


print("🎄 Day 3: Lobby")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
