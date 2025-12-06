def mergeIntervals(intervals):
    intervals.sort()
    merged_intervals = []
    for start, end in intervals:
        if not merged_intervals or start > merged_intervals[-1][1]:
            merged_intervals.append([start,end])
        else:
            merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
    return merged_intervals

def getIntervalsAndIDs(fileName):
    intervals = []
    ids = []

    with open(fileName, 'r') as f:
        for line in f:
            line = line.rstrip()
            if not line:
                break
            split_line = line.split('-')
            intervals.append([int(split_line[0]), int(split_line[1])])

        for line in f:
            ids.append(int(line.rstrip()))

    return intervals, ids

def getFreshIDs(intervals, ids):
    freshIDs = []
    for id in ids:
        for start, end in intervals:
            if start <= id <= end:
                freshIDs.append(id)
    return freshIDs

def part1(fileName):
    intervals, ids = getIntervalsAndIDs(fileName)
    mergedIntervals = mergeIntervals(intervals)
    freshIDs = getFreshIDs(mergedIntervals, ids)
    print(len(freshIDs))


def getNumFreshIDs(intervals):
    freshIDs = 0
    for start, end in intervals:
        freshIDs += end - start + 1
    return freshIDs

def part2(fileName):
    intervals, _ = getIntervalsAndIDs(fileName)
    mergedIntervals = mergeIntervals(intervals)
    numFreshIDs = getNumFreshIDs(mergedIntervals)
    print(numFreshIDs)

if __name__ == "__main__":
    part1("day5_input.txt")
    part1("day5_test_input.txt")
    print()
    part2("day5_input.txt")
    part2("day5_test_input.txt")
