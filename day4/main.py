with open("day4/input.txt", "r") as f:
    data = f.read().splitlines()


MIN_I = 0
MIN_J = 0
MAX_I = len(data)
MAX_J = len(data[0])

XMAS = ["X", "M", "A", "S"]

def check_horizontal(data: list, i: int, j: int) -> int:
    outcome = 0
    if j + 3 < MAX_J:
        if data[i][j] == "X" and data[i][j + 1] == "M" and data[i][j + 2] == "A" and data[i][j + 3] == "S":
            outcome += 1
    if j - 3 >= MIN_J:
        if data[i][j] == "X" and data[i][j - 1] == "M" and data[i][j - 2] == "A" and data[i][j - 3] == "S":
            outcome += 1
    return outcome


def check_vertical(data: list, i: int, j: int) -> int:
    outcome = 0
    if i + 3 < MAX_I:
        if data[i][j] == "X" and data[i + 1][j] == "M" and data[i + 2][j] == "A" and data[i + 3][j] == "S":
            outcome += 1
    if i - 3 >= MIN_I:
        if data[i][j] == "X" and data[i - 1][j] == "M" and data[i - 2][j] == "A" and data[i - 3][j] == "S":
            outcome += 1
    return outcome


def check_diagonal(data: list, i: int, j: int) -> int:
    outcome = 0
    if i + 3 < MAX_I and j + 3 < MAX_J:
        if data[i][j] == "X" and data[i + 1][j + 1] == "M" and data[i + 2][j + 2] == "A" and data[i + 3][j + 3] == "S":
            outcome += 1
    if i - 3 >= MIN_I and j - 3 >= MIN_J:
        if data[i][j] == "X" and data[i - 1][j - 1] == "M" and data[i - 2][j - 2] == "A" and data[i - 3][j - 3] == "S":
            outcome += 1
    if i - 3 >= MIN_I and j + 3 < MAX_J:
        if data[i][j] == "X" and data[i - 1][j + 1] == "M" and data[i - 2][j + 2] == "A" and data[i - 3][j + 3] == "S":
            outcome += 1
    if i + 3 < MAX_I and j - 3 >= MIN_J:
        if data[i][j] == "X" and data[i + 1][j - 1] == "M" and data[i + 2][j - 2] == "A" and data[i + 3][j - 3] == "S":
            outcome += 1
    return outcome


def check_for_xmas(data: list, i: int, j: int) -> int:
    outcome = 0
    outcome += check_horizontal(data, i, j)
    outcome += check_vertical(data, i, j)
    outcome += check_diagonal(data, i, j)
    return outcome


def check_diagonal_part_2(data: list, i: int, j: int) -> int:
    if i + 1 >= MAX_I or j + 1 >= MAX_J or i - 1 < MIN_I or j - 1 < MIN_J:
        return 0
    left_diagonal = []
    right_diagonal = []

    left_diagonal.append(data[i + 1][j + 1])
    left_diagonal.append(data[i - 1][j - 1])
    right_diagonal.append(data[i - 1][j + 1])
    right_diagonal.append(data[i + 1][j - 1])
    if set(left_diagonal) == set(["M", "S"]) and set(right_diagonal) == set(["M", "S"]):
        return 1
    return 0


def part_1():
    outcome = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "X":
                outcome += check_for_xmas(data, i, j)
    print(outcome)

def part_2():
    outcome = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "A":
                outcome += check_diagonal_part_2(data, i, j)
    print(outcome)

part_2()