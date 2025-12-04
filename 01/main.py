#!/usr/bin/env python3

def get_lines():
    with open(input) as fptr:
        for line in fptr.readlines():
            yield line.strip()


def parse_op(op: str) -> (int, int):
    steps = int(op[1:])
    revs = int(steps / 100)
    if op[0] == "L":
        return -1*(steps % 100), revs
    else:
        return steps % 100, revs


def add(x, y: int) -> (int, bool):
    sum = x + y
    if sum < 0 or sum > 99:
        return sum % 100, x != 0
    else:
        return sum, sum == 0


input = "input.txt"
dial = 50
zerosA = 0
zerosB = 0

for line in get_lines():
    op, revs = parse_op(line)
    dial, addOne = add(dial, op)
    zerosB += revs
    if addOne:
        zerosB += 1
    if dial == 0:
        zerosA += 1

print(zerosA)
print(zerosB)
