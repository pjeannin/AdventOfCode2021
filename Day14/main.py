#!/usr/bin/python3

from collections import defaultdict
from copy import copy
import sys


def part_one(filename):
    sys.stdin = open(filename, "r")

    s = input()
    blank = input()
    pairs = {}
    while 1:
        try:
            x, y = input().split(" -> ")
            pairs[(x[0], x[1])] = y
        except:
            break
    s = list(s)
    for __ in range(10):
        t = []
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                t += [s[i]]
                break
            if (s[i], s[i + 1]) in pairs:
                t += [s[i], pairs[(s[i], s[i + 1])]]
                i += 1
            else:
                t += [s[i]]
                i += 1
        s = list(t)
    ct = sorted(list(set([s.count(k) for k in set(s)])))
    return ct[-1] - ct[0]


def part_two(filename):
    sys.stdin = open(filename, "r")

    s = input()
    blank = input()
    pairs = {}
    while 1:
        try:
            x, y = input().split(" -> ")
            pairs[(x[0], x[1])] = y
        except:
            break
    s = list(s)
    present = defaultdict(int)
    count = [0] * 26
    for i in range(len(s)):
        count[ord(s[i]) - ord('A')] += 1
        if i == len(s) - 1:
            break
        present[(s[i], s[i + 1])] += 1
    for __ in range(40):
        present_copy = defaultdict(int)
        for x, y in present:
            if (x, y) in pairs:
                z = pairs[(x, y)]
                count[ord(z) - ord('A')] += present[(x, y)]
                present_copy[(x, z)] += present[(x, y)]
                present_copy[(z, y)] += present[(x, y)]
        present = copy(present_copy)

    ct = sorted(x for x in count if x)
    return ct[-1] - ct[0]


if __name__ == "__main__":
    print(part_one("inputFile.txt"))
    print(part_two("inputFile.txt"))
    exit(0)
