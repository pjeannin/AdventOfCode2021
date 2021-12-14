#!/usr/bin/python3

import sys


def part_one(filename):
    sys.stdin = open(filename, "r")
    points = []
    while 1:
        s = input()
        if s == "":
            break
        x, y = map(int, s.split(','))
        points += [(x, y)]

    for times in range(1):
        inst = input().split()[-1]
        val = int(inst.split('=')[-1])
        if inst.startswith('x'):
            points = list(set([(x, y) if x <= val else (2 * val - x, y) for x, y in points]))
        else:
            points = list(set([(x, y) if y <= val else (x, 2 * val - y) for x, y in points]))

    return len(points)


def part_two(filename):
    sys.stdin = open(filename, "r")
    points = []
    while 1:
        s = input()
        if s == "":
            break
        x, y = map(int, s.split(','))
        points += [(x, y)]

    for times in range(12):
        inst = input().split()[-1]
        val = int(inst.split('=')[-1])
        if inst.startswith('x'):
            points = list(set([(x, y) if x <= val else (2 * val - x, y) for x, y in points]))
        else:
            points = list(set([(x, y) if y <= val else (x, 2 * val - y) for x, y in points]))

    for y in range(max(y for x, y in points) + 1):
        for x in range(max(x for x, y in points) + 1):
            if (x - min(p for p, q in points), y - min(q for p, q in points)) in points:
                print('##', end='')
            else:
                print('  ', end='')
        print("")


if __name__ == "__main__":
    print(part_one("inputFile.txt"))
    part_two("inputFile.txt")
    exit(0)
