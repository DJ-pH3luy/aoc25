#!/usr/bin/env python3

def get_lines():
    with open(input) as fptr:
        ret = []
        for line in fptr.readlines():
            ret.append(list(line.strip()))

        return ret


def get_adj(m: list, x: int, y: int) -> int:
    adj = 0
    for j in range(-1*kernel_size, kernel_size+1):
        if y+j < 0 or y+j >= len(m):
            continue
        for i in range(-1*kernel_size, kernel_size+1):
            if x+i < 0 or x+i >= len(m[y+j]):
                continue
            if j == 0 and i == 0:
                continue
            if m[y+j][x+i] == roll:
                adj += 1

    return adj


kernel_size = 1
roll = "@"

input = "input.txt"
result = 0
m = get_lines()
while True:
    started = result
    for y in range(0, len(m)):
        for x in range(0, len(m[y])):
            if m[y][x] != roll:
                continue
            adj = get_adj(m, x, y)
            if adj < 4:
                result += 1
                m[y][x] = "."
    if started == result:
        break

print(result)
