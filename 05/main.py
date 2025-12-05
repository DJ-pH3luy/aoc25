#!/usr/bin/env python3

def load_input():
    with open(input) as fptr:
        intervals = []
        ids = []
        second_part = False
        for line in fptr.readlines():
            if not second_part:
                if line == "\n":
                    second_part = True
                    continue
                interval = line.strip().split("-")
                intervals.append((int(interval[0]), int(interval[1])))
            else:
                ids.append(int(line.strip()))

        return intervals, ids


def check_id(id: int, intervals) -> int:
    for interval in intervals:
        if id >= interval[0] and id <= interval[1]:
            return 1
    return 0


def idx1(e):
    return e[0]


def merge(intervals):
    intervals.sort(key=idx1)
    for idx in range(1, len(intervals)):
        if intervals[idx-1][1] >= intervals[idx][0] - 1:
            if intervals[idx-1][1] < intervals[idx][1]:
                intervals[idx] = (intervals[idx-1][0], intervals[idx][1])
            else:
                intervals[idx] = (intervals[idx-1][0], intervals[idx-1][1])
            intervals[idx-1] = (0, 0)

    return [e for e in intervals if e != (0, 0)]


input = "input.txt"
result = 0
intervals, ids = load_input()

for _range in merge(intervals):
    result += _range[1] - _range[0] + 1

print(result)
