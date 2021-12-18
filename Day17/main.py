#!/usr/bin/python3

import sys


def part_one(x1, x2, y1, y2):
    ans = 0
    for x in range(500):
        for y in range(500):
            xv, yv = x, y
            curX = curY = 0
            pos = False
            maxY = 0
            for times in range(500):
                curX += xv
                curY += yv
                maxY = max(maxY, curY)
                if xv > 0: xv -= 1
                if xv < 0: xv += 1
                yv -= 1
                if y1 <= curY <= y2 and x1 <= curX <= x2:
                    pos = True
                    break
            if pos:
                ans = max(ans, maxY)
    return ans


def part_two(x1, x2, y1, y2):
    ans = 0
    for x in range(-500, 500):
        for y in range(-500, 500):
            xv, yv = x, y
            curX = curY = 0
            pos = False
            maxY = 0
            for times in range(200):
                curX += xv
                curY += yv
                maxY = max(maxY, curY)
                if xv > 0: xv -= 1
                if xv < 0: xv += 1
                yv -= 1
                if y1 <= curY <= y2 and x1 <= curX <= x2:
                    pos = True
                    break
            if pos:
                ans += 1
    return ans


if __name__ == "__main__":
    x1, x2 = 56, 76
    y1, y2 = -162, -134
    print(part_one(x1, x2, y1, y2))
    print(part_two(x1, x2, y1, y2))
    exit(0)
