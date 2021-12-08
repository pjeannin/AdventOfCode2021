#!/usr/bin/python3

def part_one(data):
    _ = 0
    for line in data:
        for elem in line[1]:
            if len(elem) == 2 or len(elem) == 3 or len(elem) == 4 or len(elem) == 7:
                _ += 1
    return _


def get_data(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
        for i in range(len(data)):
            data[i] = data[i].split(' | ')
            data[i] = [data[i][0].split(' '), data[i][1].split(' ')]
    return data


if __name__ == "__main__":
    print(part_one(get_data('inputFile.txt')))
    exit(0)
