import sys

# PART 1

PART_1_TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"
PART_1_TEST_SOLUTION = 1227775554
PART_1_INPUT = "17330-35281,9967849351-9967954114,880610-895941,942-1466,117855-209809,9427633930-9427769294,1-14,311209-533855,53851-100089,104-215,33317911-33385573,42384572-42481566,43-81,87864705-87898981,258952-303177,451399530-451565394,6464564339-6464748782,1493-2439,9941196-10054232,2994-8275,6275169-6423883,20-41,384-896,2525238272-2525279908,8884-16221,968909030-969019005,686256-831649,942986-986697,1437387916-1437426347,8897636-9031809,16048379-16225280"
PART_1_TEST_SOLUTION = 35367539282

def part1(input):
    ranges = input.split(',')

    res = 0

    for r in ranges:
        lower = int(r.split('-')[0])
        upper = int(r.split('-')[1])

        for num in range(lower, upper+1):
            numLength = len(str(num))
            numString = str(num)

            if numLength % 2 == 1:
                continue
            if numString[0:numLength // 2] == numString[numLength // 2:]:
                res += num

    print(f"Part 1 result: {res}")

# PART 2

PART_2_TEST_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"
PART_2_TEST_SOLUTION = 4174379265
PART_2_INPUT = "17330-35281,9967849351-9967954114,880610-895941,942-1466,117855-209809,9427633930-9427769294,1-14,311209-533855,53851-100089,104-215,33317911-33385573,42384572-42481566,43-81,87864705-87898981,258952-303177,451399530-451565394,6464564339-6464748782,1493-2439,9941196-10054232,2994-8275,6275169-6423883,20-41,384-896,2525238272-2525279908,8884-16221,968909030-969019005,686256-831649,942986-986697,1437387916-1437426347,8897636-9031809,16048379-16225280"
PART_2_SOLUTION = ""

def part2(input):
        ranges = input.split(',')

        res = 0
        for r in ranges:
            lower = int(r.split('-')[0])
            upper = int(r.split('-')[1])

            for num in range(lower, upper+1):
                windowLength = 1
                numLength = len(str(num))
                numString = str(num)

                for windowLength in range(1, numLength // 2 + 1):
                    if numLength % windowLength != 0:
                        continue
                    for i in range(0, numLength-windowLength, windowLength):
                        window1 = numString[i : i + windowLength]
                        window2 = numString[i+windowLength : i + windowLength * 2]
                        if window1 != window2:
                            break
                    else:
                        res += num
                        break

        print(f"Part 2 result: {res}")

part1(PART_1_INPUT)
part2(PART_2_INPUT)

