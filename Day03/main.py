#!/usr/bin/python3

def part_one(lines):
    gamma = ""
    eplison = ""
    for i in range(0, len(lines[0])):
        tmp = 0
        for line in lines:
            if line[i] == '1':
                tmp += 1
            else:
                tmp -= 1
        if tmp > 0:
            gamma += "1"
            eplison += "0"
        else:
            gamma += "0"
            eplison += "1"
    return int(gamma, 2) * int(eplison, 2)


def find_oxygen(lines):
    tmp = []
    i = 0
    t = 0
    for line in lines:
        if line[i] == '1':
            t += 1
        else:
            t -= 1
    for j in range(len(lines)):
        if t >= 0 and lines[j][i] == '1' or t < 0 and lines[j][i] == '0':
            tmp.append(lines[j])
    for k in range(1, len(tmp[0])):
        t_ = tmp
        __ = 0
        for elem in t_:
            if elem[k] == '1':
                __ += 1
            else:
                __ -= 1
        for elem in t_:
            if not (__ >= 0 and elem[k] == '1' or __ < 0 and elem[k] == '0'):
                tmp.remove(elem)
        if len(tmp) == 1:
            break
    return int(tmp[0], 2)


def find_co(lines):
    tmp = []
    i = 0
    t = 0
    for line in lines:
        if line[i] == '1':
            t += 1
        else:
            t -= 1
    for j in range(len(lines)):
        if t < 0 and lines[j][i] == '1' or t >= 0 and lines[j][i] == '0':
            tmp.append(lines[j])
    for k in range(1, len(tmp[0])):
        t_ = tmp
        __ = 0
        for elem in t_:
            if elem[k] == '1':
                __ += 1
            else:
                __ -= 1
        for elem in t_:
            if not (__ < 0 and elem[k] == '1' or __ >= 0 and elem[k] == '0'):
                tmp.remove(elem)
        if len(tmp) == 1:
            break
    return int(tmp[0], 2)


def part_two(lines):
    oxygen = find_oxygen(lines)
    co2 = find_co(lines)
    return oxygen * co2


if __name__ == "__main__":
    test = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    file = open("inputFile.txt", "r")
    lines = file.read().splitlines()
    print(part_one(lines))
    print(part_two(lines))
    exit(0)
