from icecream import ic
from itertools import product
import z3


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

    def z3_solve(btns, tar):
        opt = z3.Optimize()
        vars = [z3.Int(f"btn{i}") for i, _ in enumerate(btns)]

        for var in vars:
            # Constrain var to be >= 0 !!!
            opt.add(var >= 0)

        for i in range(len(tar)):
            c_sum = z3.Sum([vars[j] for j in range(len(btns)) if i in btns[j]])
            opt.add(c_sum == tar[i])

        total = z3.Sum(vars)
        opt.minimize(total)
        opt.check()

        return opt.model().eval(total).as_long()

    for row in rows:
        buttons = row[1:-1]
        target = row[-1]
        result = z3_solve(buttons, target)
        ans += result
    return ans


print("🎄 Day 10: XXX")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
