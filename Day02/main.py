#!/usr/bin/python3

def part_one(lines):
    position = 0
    depth = 0
    for line in lines:
        if "up" in line:
            depth -= int(line.split()[1])
        elif "down" in line:
            depth += int(line.split()[1])
        else:
            position += int(line.split()[1])
    return position * depth


def part_two(lines):
    position = 0
    depth = 0
    aim = 0
    for line in lines:
        if "up" in line:
            aim -= int(line.split()[1])
        elif "down" in line:
            aim += int(line.split()[1])
        else:
            position += int(line.split()[1])
            depth += aim * int(line.split()[1])
    return position * depth


if __name__ == '__main__':
    file = open('inputFile.txt', 'r')
    lines = file.readlines()
    test = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]
    print(part_one(test))
    print(part_one(lines))
    print(part_two(test))
    print(part_two(lines))
