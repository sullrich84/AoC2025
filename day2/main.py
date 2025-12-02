from icecream import ic
from textwrap import wrap


def parseData(name="task"):
    return open(f"{name}.txt").read().splitlines()


def is_valid(input):
    id = str(input)
    if len(id) % 2 != 0:
        return False

    l = len(id) // 2
    return id[:l] == id[-l:]


def solve1(data):
    valid_ids = []
    for line in data:
        for ids in line.split(","):
            if ids == "":
                continue

            start, end = ids.split("-")
            for id in range(int(start), int(end) + 1):
                if is_valid(id):
                    valid_ids.append(id)
    return sum(valid_ids)


def is_valid2(input):
    id = str(input)
    if len(id) == 1:
        return False
    if len(set(list(str(input)))) == 1:
        return True

    l = len(id)
    for i in range(2, l - 1):
        w = wrap(id, i)
        if len(set(w)) == 1:
            return True
    return False


def solve2(data):
    valid_ids = []
    for line in data:
        for ids in line.split(","):
            if ids == "":
                continue

            start, end = ids.split("-")
            for id in range(int(start), int(end) + 1):
                if is_valid2(id):
                    valid_ids.append(id)
    return sum(valid_ids)


print("🎄 Day 2: XXX")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
