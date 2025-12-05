def mergeIntervals(intervals):
    intervals.sort()
    merged_intervals = []
    for start, end in intervals:
        if not merged_intervals or start > merged_intervals[-1][1]:
            merged_intervals.append([start,end])
        else:
            merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
    return merged_intervals

def getIntervalsAndIDs():
    intervals = []
    ids = []

    with open("day5_input.txt", 'r') as f:
        lines = [line.rstrip() for line in f]
        i = 0

        while lines[i]:
            split_line = lines[i].split('-')
            intervals.append([int(split_line[0]), int(split_line[1])])
            i += 1

        i += 1

        while i < len(lines):
            ids.append(int(lines[i]))
            i += 1
        return intervals, ids

def getFreshIDs(intervals, ids):
    freshIDs = []
    for id in ids:
        for start, end in intervals:
            if start <= id <= end:
                freshIDs.append(id)
    return freshIDs

def part1():
    intervals, ids = getIntervalsAndIDs()
    mergedIntervals = mergeIntervals(intervals)
    freshIDs = getFreshIDs(mergedIntervals, ids)
    print(len(freshIDs))
#part1()

def getNumFreshIDs(intervals):
    freshIDs = 0
    for start, end in intervals:
        freshIDs += end - start + 1
    return freshIDs

def part2():
    intervals, _ = getIntervalsAndIDs()
    mergedIntervals = mergeIntervals(intervals)
    numFreshIDs = getNumFreshIDs(mergedIntervals)
    print(numFreshIDs)
part2()
