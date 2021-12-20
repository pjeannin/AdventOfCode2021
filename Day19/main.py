#!/usr/bin/python3

import sys


def get_permutations(x, y, z):
    _ = []
    for p, q, r in [(x, y, z), (y, z, x), (z, x, y), (x, z, y), (y, x, z), (z, y, x)]:
        _ += [(p, q, r), (-p, q, r), (p, -q, r), (-p, -q, r), (p, q, -r), (-p, q, -r), (p, -q, -r), (-p, -q, -r)]
    return _


def part_one(filename):
    sys.stdin = open(filename, "r")
    data = sys.stdin.read()

    a = []

    for s in data.split("\n\n"):
        a += [[]]
        for point in s.split("\n")[1:]:
            x, y, z = map(int, point.split(","))
            a[-1] += [(x, y, z)]
    _ = set(a[0])
    a.pop(0)

    __ = True
    while __:
        __ = False
        for i in range(len(a)):
            def check(i):
                for j in range(48):
                    for x, y, z in _:
                        for x2, y2, z2 in a[i]:
                            x2, y2, z2 = get_permutations(x2, y2, z2)[j]
                            offx, offy, offz = x2 - x, y2 - y, z2 - z
                            newset = set()
                            finalset = set()
                            for xb, yb, zb in a[i]:
                                xbb, ybb, zbb = get_permutations(xb, yb, zb)[j]
                                finalset.add((xbb - offx, ybb - offy, zbb - offz))
                                if (xbb - offx, ybb - offy, zbb - offz) in _:
                                    newset.add((xb, yb, zb))
                            if len(newset) >= 12:
                                return finalset
                return None

            cc = check(i)
            if cc:
                a.pop(i)
                __ = True
                _ |= cc
                break
    return len(_)


def part_two(filename):
    sys.stdin = open(filename, "r")
    data = sys.stdin.read()

    a = []

    for s in data.split("\n\n"):
        a += [[]]
        for point in s.split("\n")[1:]:
            x, y, z = map(int, point.split(","))
            a[-1] += [(x, y, z)]
    _ = set(a[0])
    ___ = set()
    ___.add((0, 0, 0))
    a.pop(0)

    __ = True
    while __:
        __ = False
        for i in range(len(a)):
            def check(i):
                for j in range(48):
                    for x, y, z in _:
                        for x2, y2, z2 in a[i]:
                            x2, y2, z2 = get_permutations(x2, y2, z2)[j]
                            offx, offy, offz = x2 - x, y2 - y, z2 - z
                            newset = set()
                            finalset = set()
                            for xb, yb, zb in a[i]:
                                xbb, ybb, zbb = get_permutations(xb, yb, zb)[j]
                                finalset.add((xbb - offx, ybb - offy, zbb - offz))
                                if (xbb - offx, ybb - offy, zbb - offz) in _:
                                    newset.add((xb, yb, zb))
                            if len(newset) >= 12:
                                ___.add((offx, offy, offz))
                                return finalset
                return None

            cc = check(i)
            if cc:
                a.pop(i)
                __ = True
                _ |= cc
                break

    res = 0
    for x, y, z in ___:
        for x2, y2, z2 in ___:
            res = max(res, abs(x - x2) + abs(y - y2) + abs(z - z2))
    return res


if __name__ == '__main__':
    print(part_one('inputFile.txt'))
    print(part_two('inputFile.txt'))
    exit(0)
