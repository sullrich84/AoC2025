from math import prod
import re


def parseData(name="task"):
    file = open(f"{name}.txt").read().splitlines()
    col_length = list(map(len, re.sub(r"\s([+*])", r",\1", file[-1]).split(",")))
    ops = list(re.split(r"\s+", file[-1])[:-1])
    nums, rows = ([], len(file[:-1]))

    for r in range(rows):
        col_nums, offset = ([], 0)
        for cl in col_length:
            col_nums.append(file[r][offset : offset + cl])
            offset += cl + 1
        nums.append(col_nums)

    data = list(zip(*nums))
    return (data, ops, col_length)


def parseData2(name="task"):
    file = open(f"{name}.txt").read().splitlines()
    return file


def solve1(input):
    data, ops, _ = input
    ans = 0

    for i, line in enumerate(data):
        t = 0
        for n in line:
            if ops[i] == "*":
                t = int(n) if t == 0 else t * int(n)
            else:
                t += int(n)
        ans += t

    return ans


def solve2(input):
    data, ops, col_length = input
    ans = 0

    for i, line in enumerate(data):
        c_len, nums = (col_length[i], [])
        for l in range(c_len):
            nums.append(int("".join([c[l] for c in line])))
        if ops[i] == "*":
            ans += prod(nums)
        else:
            ans += sum(nums)
    return ans


print("🎄 Day 6: Trash Compactor")
print("Part 1:", solve1(parseData("sample")))
print("Part 2:", solve2(parseData("sample")))
