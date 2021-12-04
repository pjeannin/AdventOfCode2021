#!/usr/bin/python3

def comma_separated_list_to_int_list(string):
    return [int(i) for i in string.split(",")]


def get_boards(lines):
    _ = []
    __ = []
    for i in range(2, len(lines)):
        if lines[i] == "":
            _.append(__)
            __ = []
        else:
            ___ = []
            splitted = lines[i].split(" ")
            for j in range(0, len(splitted)):
                if splitted[j] != "":
                    ___.append(int(splitted[j]))
            __.append(___)
    _.append(__)
    return _


def get_score(board, number):
    score = 0
    for b in board:
        for n in b:
            if n < 1000:
                score += n
    return score * number


def part_one(numbers, boards):
    for number in numbers:
        for board in boards:
            for i in range(0, len(board)):
                for j in range(0, len(board[i])):
                    if board[i][j] == number:
                        board[i][j] += 1000
            for i in range(0, len(board)):
                if (board[i][0] >= 1000) and (board[i][1] >= 1000) and (board[i][2] >= 1000) and (board[i][3] >= 1000) and (board[i][4] >= 1000):
                    return get_score(board, number)
                if (board[0][i] >= 1000) and (board[1][i] >= 1000) and (board[2][i] >= 1000) and (board[3][i] >= 1000) and (board[4][i] >= 1000):
                    return get_score(board, number)


def part_two(numbers, boards):
    _ = []
    for number in numbers:
        print("###########################")
        print(number)
        print("number of board")
        print(len(boards))
        print("###########################")
        for board in boards:
            print("i")
            for i in range(0, len(board)):
                for j in range(0, len(board[i])):
                    if board[i][j] == number:
                        board[i][j] += 1000
            for i in range(0, len(board)):
                print(board[0][i])
                print(board[1][i])
                print(board[2][i])
                print(board[3][i])
                print(board[4][i])
                print("")
                if (board[i][0] >= 1000) and (board[i][1] >= 1000) and (board[i][2] >= 1000) and (board[i][3] >= 1000) and (board[i][4] >= 1000):
                    print(number)
                    _.append(get_score(board, number))
                    try:
                        boards.remove(board)
                    except:
                        pass
                if (board[0][i] >= 1000) and (board[1][i] >= 1000) and (board[2][i] >= 1000) and (board[3][i] >= 1000) and (board[4][i] >= 1000):
                    print(number)
                    _.append(get_score(board, number))
                    try:
                        boards.remove(board)
                    except:
                        pass
    return _[-1]


if __name__ == "__main__":
    testFile = open("test.txt", "r")
    file = open("inputFile.txt", "r")
    data = file.read().splitlines()
    testData = testFile.read().splitlines()
    numbers = comma_separated_list_to_int_list(data[0])
    boards = get_boards(data)
    print(part_two(numbers, boards))
    print(part_one(numbers, boards))
