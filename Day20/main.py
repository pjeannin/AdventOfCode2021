#!/usr/bin/python3

import sys


def part_one(filename):
    sys.stdin = open(filename, "r")

    s = input()
    _ = input()
    a = []
    while 1:
        try:
            line = input()
            a += [list('.' * 1000 + line + '.' * 1000)]
        except EOFError:
            break
    for i in range(1000):
        a = ['.' * len(a[-1])] + a + ['.' * len(a[-1])]
    n, m = len(a), len(a[0])
    for __ in range(2):
        b = [[''] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                val = 256 * (a[(i - 1) % n][(j - 1) % m] == '#') + \
                      128 * (a[(i - 1) % n][j] == '#') + \
                      64 * (a[(i - 1) % n][(j + 1) % m] == '#') + \
                      32 * (a[i][(j - 1) % m] == '#') + \
                      16 * (a[i][j] == '#') + \
                      8 * (a[i][(j + 1) % m] == '#') + \
                      4 * (a[(i + 1) % n][(j - 1) % m] == '#') + \
                      2 * (a[(i + 1) % n][j] == '#') + \
                      1 * (a[(i + 1) % n][(j + 1) % m] == '#')
                b[i][j] = s[val]
        a = [list(x) for x in b]
    return sum(x.count("#") for x in a)


def part_two(filename):
    sys.stdin = open(filename, "r")

    s = input()
    _ = input()
    a = []
    while 1:
        try:
            line = input()
            a += [list('.' * 5000 + line + '.' * 5000)]
        except EOFError:
            break
    for i in range(5000):
        a = ['.' * len(a[-1])] + a + ['.' * len(a[-1])]
    n, m = len(a), len(a[0])
    for __ in range(50):
        b = [[''] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                val = 256 * (a[(i - 1) % n][(j - 1) % m] == '#') + \
                      128 * (a[(i - 1) % n][j] == '#') + \
                      64 * (a[(i - 1) % n][(j + 1) % m] == '#') + \
                      32 * (a[i][(j - 1) % m] == '#') + \
                      16 * (a[i][j] == '#') + \
                      8 * (a[i][(j + 1) % m] == '#') + \
                      4 * (a[(i + 1) % n][(j - 1) % m] == '#') + \
                      2 * (a[(i + 1) % n][j] == '#') + \
                      1 * (a[(i + 1) % n][(j + 1) % m] == '#')
                b[i][j] = s[val]
        a = [list(x) for x in b]
    return sum(x.count("#") for x in a)


if __name__ == "__main__":
    print(part_one('inputFile.txt'))
    print(part_two('inputFile.txt'))
    exit(0)
