def parseData(name="task"):
    return [list(line) for line in open(f"{name}.txt").read().splitlines()]


dirs = [
    (-1, -1),
    (-1, 0),
    (-1, +1),
    (0, -1),
    (0, +1),
    (+1, -1),
    (+1, 0),
    (+1, +1),
]


def rearrange(grid):
    rMax, cMax, movable = (len(grid), len(grid[0]), set())
    for r in range(0, rMax):
        for c in range(0, cMax):
            paperrolls = 0
            if grid[r][c] != "@":
                continue
            for dr, dc in dirs:
                nr, nc = (r + dr, c + dc)
                if nr < 0 or nr >= rMax or nc < 0 or nc >= cMax:
                    continue
                if grid[nr][nc] == "@":
                    paperrolls += 1
            if paperrolls < 4:
                movable.add((r, c))

    return movable


def solve1(grid):
    return len(rearrange(grid))


def solve2(grid):
    removed = 0
    while True:
        movable = rearrange(grid)
        if len(movable) == 0:
            return removed
        for r, c in movable:
            grid[r][c] = "."
            removed += 1


print("🎄 Day 4: Printing Department")
print("Part 1:", solve1(parseData("task")))
print("Part 2:", solve2(parseData("task")))
