#!/usr/bin/python3

import sys


def sole_part_one(cur, en, graph, di2, vis=None):
    if cur == en:
        return 1
    ans = 0
    for x in graph[cur]:
        if not di2[x].lower() == di2[x]:
            ans += sole_part_one(x, en, graph, di2, list(vis) + [x])
        else:
            if x not in vis:
                ans += sole_part_one(x, en, graph, di2, list(vis) + [x])
    return ans


def part_one(filename):
    sys.stdin = open(filename, "r")

    graph = [[] for __ in range(1000)]
    di = {}
    di2 = {}
    while 1:
        try:
            x, y = list(map(str, input().split('-')))
            if x not in di:
                di[x] = len(di)
                di2[len(di) - 1] = x
            if y not in di:
                di[y] = len(di)
                di2[len(di) - 1] = y
            graph[di[x]].append(di[y])
            graph[di[y]].append(di[x])
        except:
            break

    st, en = di["start"], di["end"]
    return sole_part_one(st, en, graph, di2, list([st]))


def solve_part_two(cur, en, graph, di2, vis=None):
    if cur == en:
        return 1
    ans = 0
    for x in graph[cur]:
        if not di2[x].lower() == di2[x]:
            ans += solve_part_two(x, en, graph, di2, list(vis) + [x])
        else:
            if di2[x] in ['start', 'end']:
                if x not in vis:
                    ans += solve_part_two(x, en, graph, di2, list(vis) + [x])
                continue
            pos = 1
            for y in vis:
                if di2[y].lower() == di2[y] and vis.count(y) > 1:
                    pos -= 1
                    break
            if pos == 1 or vis.count(x) == 0:
                ans += solve_part_two(x, en, graph, di2, list(vis) + [x])
    return ans


def part_two(filename):
    sys.stdin = open(filename, "r")

    graph = [[] for __ in range(1000)]
    di = {}
    di2 = {}
    while 1:
        try:
            x, y = list(map(str, input().split('-')))
            if x not in di:
                di[x] = len(di)
                di2[len(di) - 1] = x
            if y not in di:
                di[y] = len(di)
                di2[len(di) - 1] = y
            graph[di[x]].append(di[y])
            graph[di[y]].append(di[x])
        except:
            break

    st, en = di["start"], di["end"]
    return solve_part_two(st, en, graph, di2, list([st]))


if __name__ == "__main__":
    print(part_one("inputFile.txt"))
    print(part_two("inputFile.txt"))
    exit(0)
