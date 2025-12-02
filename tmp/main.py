from icecream import ic


def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def solve1(data):
    ic(data)


def solve2(data):
    pass


print("🎄 Day 0: XXX")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
