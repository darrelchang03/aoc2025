from math import sqrt
from math import prod as product

TEST_INPUT = "day8_test_input.txt"
TEST_K = 10

INPUT = "day8_input.txt"
K = 1000

def computeDistance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def getCoordinates(fileName):
    with open(fileName, 'r') as f:
        return [[int(x) for x in line.strip().split(',')] for line in f.readlines()]

def getTopKClosestCoordinates(coords, k):
    pairs = []
    for i, coord1 in enumerate(coords):
        for _, coord2 in enumerate(coords[i+1:]):
            pairs.append((tuple(coord1), tuple(coord2)))
    pairs.sort(key= lambda pair: computeDistance(pair[0], pair[1]))
    return pairs[:k]

def part1(pairs):
    circuits = []
    for p1, p2 in pairs:
        found = []
        for circuit in circuits:
            if p1 in circuit or p2 in circuit:
                found.append(circuit)
        if not found:
            circuits.append({p1, p2})
        else:
            merged = {p1, p2}
            for c in found:
                merged |= c
                circuits.remove(c)
            circuits.append(merged)

    circuitSizes = [len(circuit) for circuit in circuits]
    circuitSizes.sort(reverse=True)
    return product(circuitSizes[:3])

coords = getCoordinates(INPUT)
sorted = getTopKClosestCoordinates(coords, K)
circuits = part1(sorted)
print(circuits)

