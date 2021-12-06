#!/usr/bin/python3

def convert(input):
    input = input.split(",")
    input = [int(x) for x in input]
    return input


def part_one(data):
    for _ in range(256):
        for i in range(len(data)):
            data[i] -= 1
        for i in range(len(data)):
            if data[i] == -1:
                data[i] = 6
                data.append(8)
    return len(data)


if __name__ == "__main__":
    file = open("inputFile.txt", "r")
    datas = convert(file.read())
    test = [3, 4, 3, 1, 2]
    print(part_one(test))
