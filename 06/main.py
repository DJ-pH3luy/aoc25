#!/usr/bin/env python3

def load_input():
    with open(input) as fptr:
        ret = []
        for line in fptr.readlines():
            ret.append([e for e in line.split(" ")
                        if e != " " and e != "" and e != "\n"])

        return ret


def load_as_matrix():
    with open(input) as fptr:
        ret = []
        for line in fptr.readlines():
            ret.append(line)
        return ret


def next_problem(m, start):
    for idx in range(start+1, len(m[word_size])):
        if m[word_size][idx] != " ":
            return idx, m[word_size][start]
    return -1, ""


def get_numbers(m, idx, next):
    for x in range(idx, next):
        num = ""
        for y in range(word_size):
            num += m[y][x]
        if num.strip() == "":
            continue
        yield int(num)


input = "input.txt"
word_size = 4
m = load_as_matrix()
result = 0
idx = 0
while True:
    next, op = next_problem(m, idx)
    if next == -1:
        break
    if op == "+":
        for num in get_numbers(m, idx, next):
            result += num
    else:
        mul = 1
        for num in get_numbers(m, idx, next):
            mul *= num
        result += mul

    idx = next

print(result)

# problems = load_input()
# for idx in range(len(problems[0])):
#     if problems[4][idx] == "+":
#         for num in range(4):
#             result += int(problems[num][idx])
#     else:
#         mul = 1
#         for num in range(4):
#             mul *= int(problems[num][idx])
#         result += mul
#
# print(result)
