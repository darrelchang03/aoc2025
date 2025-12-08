def parseLines(fileName):
    with open(fileName, 'r') as f:
        return [line.split() for line in f.readlines()]

def part1(lines):
    res = 0
    for j in range(len(lines[0])):
        acc = 0
        for i in range(len(lines[:-1])):
            operator = lines[-1][j] 
            match operator:
                case "+":
                    if not acc:
                        acc = int(lines[i][j])
                    else:
                        acc += int(lines[i][j])
                case "*":
                    if not acc:
                        acc = int(lines[i][j])
                    else:
                        acc *= int(lines[i][j])
        res += acc
    return res
lines = parseLines("day6_input.txt")
res = part1(lines)
print(res)
