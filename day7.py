from sys import maxsize
from functools import lru_cache


def getLines(fileName):
    with open(fileName, 'r') as f:
        return [line.rstrip() for line in f.readlines()]

def part1(fileName):
    lines = getLines(fileName)
    searched = set()
    def dfs(i, j):
        if i >= len(lines) or j < 0 or j >= len(lines[0]):
            return 0
        if (i,j) in searched:
            return 0
        searched.add((i,j))
        if lines[i][j] == "^":
            return 1 + dfs(i+1, j-1) + dfs(i+1, j+1)
        return dfs(i+1, j)
    j = lines[0].find("S")
    return dfs(0, j)

def part2(fileName):
    lines = getLines(fileName)
    @lru_cache(maxsize=None)
    def dfs(i, j):
        if j < 0 or j >= len(lines[0]):
            return 0
        if i >= len(lines):
            return 1
        if lines[i][j] == "^":
            return dfs(i+1, j+1) + dfs(i+1, j-1)
        else:
            return dfs(i+1, j)

    j = lines[0].find("S")
    return dfs(0, j)

part1Res = part1("day7_input.txt")
print(f"Part 1 Result: {part1Res}")

part2Res = part2("day7_input.txt")
print(f"Part 2 Result: {part2Res}")
