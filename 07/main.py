#!/usr/bin/env python3

def load_matrix():
    with open(input) as fptr:
        ret = []
        for line in fptr.readlines():
            ret.append(list(line))
        return ret


def write_cell(m, x, y, p):
    cell = m[y][x]
    if cell == ".":
        m[y][x] = p
    else:
        m[y][x] = str(int(cell)+int(p))


def process_cell(m, x, y):
    cell = m[y][x]
    if cell == "\n":
        return 0
    if cell == "S":
        m[y+1][x] = "1"
        return 0
    if cell != "." and cell != "^":
        if m[y+1][x] == "^":
            write_cell(m, x-1, y+1, cell)
            write_cell(m, x+1, y+1, cell)
            return 1
        else:
            write_cell(m, x, y+1, cell)

    return 0


input = "input.txt"
m = load_matrix()
splits = 0
beams = 0

for y in range(0, len(m)-1):
    for x in range(0, len(m[y])):
        splits += process_cell(m, x, y)

for x in m[-1]:
    if x != "." and x != "^" and x != "\n":
        beams += int(x)

print(splits)
print(beams)
