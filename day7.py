def part1(fileName):
    with open(fileName, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
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
res = part1("day7_input.txt")
print(res)
