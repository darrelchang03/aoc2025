def parseLinesPart1(fileName):
    with open(fileName, 'r') as f:
        return [line.split() for line in f.readlines()]

def parseLinesPart2(fileName):
    with open(fileName, 'r') as f:
        input_data = f.read()
        data = input_data.splitlines()
        nums = [ ''.join(num) for num in zip(*data[:-1])]
        ops = data[-1].split()
        return nums, ops

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

def part2(nums, ops):
    i = 0
    op = ops[i]
    res = 0
    acc = 0
    for num in nums:
        if not num.strip():
            i += 1
            op = ops[i]
            res += acc
            acc = 0
            continue
        num = int(num)
        if op == "*":
            if acc:
                acc *= num
            else:
                acc = num
        if op == "+":
            if acc:
                acc += num
            else:
                acc = num
    res += acc
    return res

if __name__ == "__main__":
    lines = parseLinesPart1("day6_test_input.txt")
    print(lines)
    part1Res = part1(lines)
    print(part1Res)

    nums, ops = parseLinesPart2("day6_input.txt")
    part2Res = part2(nums, ops)
    print(part2Res)
