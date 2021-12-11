#!/usr/bin/python3

def part_one(data):
    res = 0
    for _ in range(100):
        pos = False
        for i in range(10):
            for j in range(10):
                data[i][j] += 1
                pos |= (data[i][j] > 9)

        while pos:
            b = [[0] * 10 for __ in range(10)]
            pos = False
            for i in range(10):
                for j in range(10):
                    if data[i][j] > 9:
                        res += 1
                        continue
                    if data[i][j] == 0: continue
                    flag = False
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx == dy == 0: continue
                            if 0 <= i + dx < 10 and 0 <= j + dy < 10 and data[i + dx][j + dy] > 9:
                                flag += 1
                    b[i][j] = data[i][j] + flag
                    pos |= (b[i][j] > 9)
            for i in range(10):
                data[i] = list(b[i])

    return res


def part_two(data):
    res = 0
    while 1:
        pos = False
        for i in range(10):
            for j in range(10):
                data[i][j] += 1
                pos |= (data[i][j] > 9)

        while pos:
            b = [[0] * 10 for __ in range(10)]
            pos = False
            for i in range(10):
                for j in range(10):
                    if data[i][j] > 9:
                        continue
                    if data[i][j] == 0: continue
                    flag = False
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx == dy == 0: continue
                            if 0 <= i + dx < 10 and 0 <= j + dy < 10 and data[i + dx][j + dy] > 9:
                                flag += 1
                    b[i][j] = data[i][j] + flag
                    pos |= (b[i][j] > 9)
            for i in range(10):
                data[i] = list(b[i])
        for elem in data:
            print(elem)
        print()
        if not sum(sum(data[i]) for i in range(10)):
            return res + 1
        res += 1


if __name__ == "__main__":
    file = open("test.txt", "r")
    lines = file.read().splitlines()
    file.close()
    data = []
    for line in lines:
        data.append([int(x) for x in line])
    print(part_one(data))
    print(part_two(data))
    exit(0)
