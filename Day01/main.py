#!/usr/bin/python3

def part_one(depth_list):
    count    = 0
    for i in range(1, len(depth_list)):
        if depth_list[i] > depth_list[i-1]:
            count += 1
    return count


def part_two(depth_list):
    count = 0
    for i in range(1, len(depth_list) - 2):
        if depth_list[i-1] + depth_list[i] + depth_list[i+1] < depth_list[i] + depth_list[i+1] + depth_list[i+2]:
            count += 1
    return count


if __name__ == "__main__":
    file = open("inputFile.txt", "r")
    depth_list = []
    for line in file:
        depth_list.append(int(line))
    print(part_one(depth_list))
    print(part_two(depth_list))
