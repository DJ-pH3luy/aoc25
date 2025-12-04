#!/usr/bin/env python3

def load_input():
    with open(input) as fptr:
        data = fptr.read()
        for _range in data.split(","):
            id_range = _range.split("-")
            yield int(id_range[0]), int(id_range[1])


def is_invalid(s) -> bool:
    for x in range(2, len(s)+1):
        if len(s) % x == 0:
            # to solve A, uncomment
            # if x != 2:
            #     continue
            sub_len = int(len(s) / x)
            sub_strings = [s[i:i+sub_len] for i in range(0, len(s), sub_len)]
            comp = ""
            match = True
            for sub_str in sub_strings:
                if comp == "":
                    comp = sub_str
                    continue
                if comp != sub_str:
                    match = False
                    break
            if match:
                return True

    return False


input = "input.txt"
result = 0
for set in load_input():
    for id in range(set[0], set[1]+1):
        if is_invalid(str(id)):
            result += id

print(result)
