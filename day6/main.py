from icecream import ic
from collections import defaultdict
import re


def parseData1(name="task"):
    file = open(f"{name}.txt").read().splitlines()
    return [re.findall(r"\d+|[+*]", z) for z in file]


def parseData2(name="task"):
    file = open(f"{name}.txt").read().splitlines()
    return file


def solve1(data):
    ops = data[-1]
    stack = {}
    for line in data[:-1]:
        for i, n in enumerate(line):
            if i not in stack:
                stack[i] = int(n)
            else:
                if ops[i] == "+":
                    stack[i] += int(n)
                else:
                    stack[i] *= int(n)
    return sum(stack.values())


def solve2(data):
    ops = data[-1]
    col = -1
    length = defaultdict(int)
    operations = []
    for char in list(ops):
        if char in ["+", "*"]:
            operations.append(char)
            col += 1
        length[col] += 1

    for k in list(length.keys())[:-1]:
        length[k] -= 1

    matrix = defaultdict(list)
    for line in data[:-1]:
        off = 0
        for col, line_length in enumerate(length.values()):
            num = line[off : off + line_length]
            matrix[col].append(num)
            off += line_length + 1

    m_cols = len(matrix[0])
    m_rows = len(matrix)
    m_vals = list(matrix.values())

    res = []
    for row in range(m_rows):
        numbers = defaultdict(str)
        for col in range(m_cols):
            col_length = len(m_vals[row][col])
            for i in range(col_length):
                char = m_vals[row][col][i]
                if char != " ":
                    numbers[i] += char
        res.append(numbers.values())

    ans = 0
    for i, nums in enumerate(res):
        total = 0
        for n in nums:
            if operations[i] == "+":
                total += int(n)
            else:
                if total == 0:
                    total = int(n)
                else:
                    total *= int(n)
        ans += total

    return ans


print("🎄 Day 6: XXX")
print("Part 1:", solve1(parseData1("task")))
print("Part 2:", solve2(parseData2("task")))
