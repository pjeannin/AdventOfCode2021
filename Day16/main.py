#!/usr/bin/python3

import sys


def get_sum_part_one(s, i=0):
    version = int(s[i:(i+3)], 2)
    type_id = int(s[(i+3):(i+6)], 2)
    if type_id == 4:
        i += 6
        while s[i] == '1':
            i += 5
        return i + 4, version
    length_type = int(s[i+6])
    if length_type == 0:
        sub_length = int(s[(i+7):(i+7+15)], 2)
        i += 7 + 15
        j = i
        ans = version
        while j != i + sub_length:
            j, val = get_sum_part_one(s, j)
            j += 1
            ans += val
        return j - 1, ans
    else:
        sub_count = int(s[(i+7):(i+7+11)], 2)
        i += 7 + 11
        j = i
        ans = version
        while sub_count:
            sub_count -= 1
            j, val = get_sum_part_one(s, j)
            j += 1
            ans += val
        return j - 1, ans


def get_sum_part_two(s, i=0):
    version = int(s[i:(i + 3)], 2)
    type_id = int(s[(i + 3):(i + 6)], 2)
    if type_id == 4:
        i += 6
        value = ""
        while s[i] == '1':
            value += s[(i + 1):(i + 5)]
            i += 5
        value += s[(i + 1):(i + 5)]
        return i + 4, int(value, 2)
    length_type = int(s[i + 6])
    values = []
    if length_type == 0:
        sub_length = int(s[(i + 7):(i + 7 + 15)], 2)
        i += 7 + 15
        j = i
        ans = version
        while j != i + sub_length:
            j, val = get_sum_part_two(s, j)
            j += 1
            ans += val
            values += [val]
    else:
        sub_count = int(s[(i + 7):(i + 7 + 11)], 2)
        i += 7 + 11
        j = i
        ans = version
        while sub_count:
            sub_count -= 1
            j, val = get_sum_part_two(s, j)
            j += 1
            ans += val
            values += [val]

    if type_id == 0:
        result = sum(values)
    if type_id == 1:
        result = 1
        for value in values:
            result *= value
    if type_id == 2:
        result = min(values)
    if type_id == 3:
        result = max(values)
    if type_id == 5:
        result = values[0] > values[1]
    if type_id == 6:
        result = values[0] < values[1]
    if type_id == 7:
        result = values[0] == values[1]
    return j - 1, result


def make4(s):
    return "0" * (4 - len(s)) + s


def part_one(filename):
    sys.stdin = open(filename, 'r')
    s = "".join(make4(bin(int(x, 16))[2:]) for x in input())
    finish_index, total = get_sum_part_one(s)
    return total


def part_two(filename):
    sys.stdin = open(filename, 'r')
    s = "".join(make4(bin(int(x, 16))[2:]) for x in input())
    finish_index, total = get_sum_part_two(s)
    return total


if __name__ == "__main__":
    print(part_one("inputFile.txt"))
    print(part_two("inputFile.txt"))
    exit(0)
