#!/usr/bin/python3

def part_one(data):
    _ = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if (i == 0 or i > 0 and data[i][j] < data[i - 1][j]) and (i == len(data) - 1 or i < len(data) - 1 and data[i][j] < data[i + 1][j]) and (j == 0 or j > 0 and data[i][j] < data[i][j - 1]) and (j == len(data[i]) - 1 or j < len(data[i]) - 1 and data[i][j] < data[i][j + 1]):
                _.append(data[i][j])
    res = 0
    for i in _:
        res += i + 1
    return res


def part_two(data):
    return part_one(data)


if __name__ == '__main__':
    file = open('inputFile.txt', 'r')
    data = file.read().splitlines()
    file.close()
    for i in range(len(data)):
        data[i] = [int(x) for x in data[i]]
    print(part_one(data))
    exit(0)
