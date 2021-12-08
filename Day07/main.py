#!/usr/bin/python3


def solve(input_positions):
    positions = [int(x) for x in input_positions.split(",")]
    min_position = min(positions)
    max_position = max(positions)
    min_cost = None
    for i in range(min_position, max_position + 1):
        cost = 0
        for position in positions:
            cost += abs(i - position)
        if min_cost is None or cost < min_cost:
            min_cost = cost
    return min_cost


def solve_two(input_positions):
    positions = [int(x) for x in input_positions.split(",")]
    min_position = min(positions)
    max_position = max(positions)
    min_cost = None
    for i in range(min_position, max_position + 1):
        cost = 0
        for position in positions:
            for j in range(1, abs(i - position) + 1):
                cost += j
        if min_cost is None or cost < min_cost:
            min_cost = cost
    return min_cost


if __name__ == '__main__':
    test = "16,1,2,0,4,2,7,1,2,14"
    file = open("inputFile.txt", "r")
    line = file.readline()
    print(solve(line))
    print(solve_two(line))
    exit(0)
