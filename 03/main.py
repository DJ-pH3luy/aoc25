#!/usr/bin/env python3

def get_lines():
    with open(input) as fptr:
        for line in fptr.readlines():
            yield line.strip()


def find_max(line: str) -> (int, int):
    max = 0
    idx = 0
    for x in range(0, len(line)):
        if int(line[x]) > max:
            max = int(line[x])
            idx = x
    return max, idx


input = "input.txt"
battery_count = 12  # = 2 for A
result = 0

for line in get_lines():
    marker = 0
    res = ""
    for x in range(battery_count-1, -1, -1):
        max, idx = find_max(line[marker:len(line)-x])
        marker += idx + 1
        res += str(max)

    result += int(res)

print(result)
