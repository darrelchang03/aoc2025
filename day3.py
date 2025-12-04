"""
Test input:
    987654321111111
    811111111111119
    234234234234278
    818181911112111
Test answer: 357
"""

from os import wait


def getBankMaxPart1(line: str) -> int:
    res = 0
    if len(line) == 1:
        return int(line)
    l = 0
    for r in range(1, len(line)):
        res = max(res, int(line[l] + line[r]))
        if int(line[r]) > int(line[l]):
            l = r
    return res
    
def getBatteryTotalPart1(input: list[str]):
    totalJoltage = 0
    for line in input:
        got = getBankMaxPart1(line)
        totalJoltage += got
    return totalJoltage

test_input=["987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111"]

#print(part3(test_input))
#print(f"Expected: 357")

def part1():
    with open("day3_input.txt", 'r') as f:
        lines = f.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.rstrip('\n'))
        lines = stripped_lines

        totalJoltage = getBatteryTotalPart1(lines)
        print(f"Part 1 answer: {totalJoltage}")

def getBankMaxPart2(line: str):
    # greedy approach. 
    # window size = len(line) - totalSelected + 1
    # select max val in window
    # reduce window by distance between selected and l
    l = 0
    r = len(line) - 12
    curr = ""
    while r < len(line):
        selectedIndex = -1
        maxVal = 0
        for i, num in enumerate(line[l:r+1]):
            if int(num) > maxVal:
                maxVal = int(num)
                selectedIndex = i + l
        curr += str(maxVal)

        l = selectedIndex + 1
        r = l + r - selectedIndex
    return int(curr)

def getBatteryTotalPart2(input: list[str]):
    totalJoltage = 0
    for line in input:
        got =  getBankMaxPart2(line)
        #print(got)
        totalJoltage += got 
    return totalJoltage

def part2():
    with open("day3_input.txt", 'r') as f:
        lines = f.readlines()
        stripped_lines = []
        for line in lines:
            stripped_lines.append(line.rstrip('\n'))
        lines = stripped_lines

        totalJoltage = getBatteryTotalPart2(lines)
        print(f"Part 2 answer: {totalJoltage}")
part2()

