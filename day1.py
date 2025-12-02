# PART 1
import sys

# mod 100
# If dial points at 0 -> += res

dial = 50
res = 0

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    lines = f.readlines()

    for line in lines:
        if line[0] == "R":
            dial = (dial + int(line[1:])) % 100
        elif line[0] == "L":
            dial = (dial - int(line[1:])) % 100
        if dial == 0:
            res += 1

print(f"Part 1 password is: {res}")

# PART 2

dial = 50
res = 0

file_name = sys.argv[1]

with open(file_name, 'r') as f:
    lines = f.readlines()

    for line in lines:
        moves = int(line[1:])
        if line[0] == "R":
            clicks = ((dial + moves) // 100) - ((dial) // 100)
            res += clicks
            dial = (dial + moves) % 100
        elif line[0] == "L":
            clicks = ((dial-1) // 100) - ((dial - moves - 1) // 100)
            res += clicks
            dial = (dial - moves) % 100

print(f"Part 2 password is: {res}")
