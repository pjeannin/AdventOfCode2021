#!/usr/bin/python3

def check_line(line):
    opened = []
    for char in line:
        if char in '([{<':
            opened.append(char)
        else:
            if len(opened) == 0:
                if char == ')':
                    return 3
                elif char == ']':
                    return 57
                elif char == '}':
                    return 1197
                else:
                    return 25137
            if (char == ')' and opened[-1] == '(') or (char == ']' and opened[-1] == '[') or (char == '}' and opened[-1] == '{') or (char == '>' and opened[-1] == '<'):
                opened.pop()
            else:
                if char == ')':
                    return 3
                elif char == ']':
                    return 57
                elif char == '}':
                    return 1197
                else:
                    return 25137
    return 0


def part_one(data):
    _ = 0
    for line in data:
        _ += check_line(line)
    return _


def check_part_two_line(line):
    _ = 0
    opened = []
    for char in line:
        if char in '([{<':
            opened.append(char)
        else:
            if len(opened) == 0:
                return _
            if (char == ')' and opened[-1] == '(') or (char == ']' and opened[-1] == '[') or (
                    char == '}' and opened[-1] == '{') or (char == '>' and opened[-1] == '<'):
                opened.pop()
            else:
                return _
    for i in range(1, len(opened) + 1):
        _ *= 5
        if opened[-i] == '(':
            _ += 1
        elif opened[-i] == '[':
            _ += 2
        elif opened[-i] == '{':
            _ += 3
        elif opened[-i] == '<':
            _ += 4
    return _


def part_two(data):
    _ = []
    for line in data:
        tmp = check_part_two_line(line)
        if tmp != 0:
            _.append(tmp)
    _.sort()
    return _[int(len(_) / 2)]


if __name__ == "__main__":
    file = open("inputFile.txt", "r")
    data = file.read().splitlines()
    print(part_one(data))
    print(part_two(data))
    exit(0)
