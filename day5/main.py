from collections import defaultdict
from typing import Tuple

with open("day5/input.txt", "r") as f:
    data = f.read().splitlines()


def check_row_with_conditions(data: str, conditions: dict[str, list[str]]) -> Tuple[bool, int]:
    numbers = data.split(",")
    for i, number in enumerate(numbers):
        if number not in conditions or i == 0:
            continue
        for x in numbers[:i]:
            if x in conditions[number]:
                return False, 0

    return True, int(numbers[len(numbers) // 2])


def part_1():
    conditions = defaultdict(list)
    put_conditions = True
    outcome = 0
    for row in data:
        if row == "":
            put_conditions = False
            continue
        if put_conditions:
            before, after = row.split("|")
            conditions[before].append(after)
        else:
            is_ok, middle_number = check_row_with_conditions(row, conditions)
            if is_ok:
                outcome += middle_number
    print(outcome)


def get_index_of_number(numbers: list[str], x: str) -> int:
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] == x:
            return i


def check_row_with_conditions_part_2(data: str, conditions: dict[str, list[str]]) -> Tuple[bool, int]:
    numbers = data.split(",")
    incorrect = False
    for i, number in enumerate(numbers):
        if number not in conditions or i == 0:
            continue
        for x in numbers[:i]:
            if x in conditions[number]:
                incorrect = True
                break
        if incorrect: 
            break
    if not incorrect:
        return False, 0

    corrected_numbers = []
    for i, number in enumerate(numbers):
        if i == 0:
            corrected_numbers.append(number)
            continue
        did = False
        for index, corrected_number in enumerate(corrected_numbers):
            if number not in conditions[corrected_number]:
                corrected_numbers.insert(index, number)
                did = True
                break
        if not did:
            corrected_numbers.append(number)

    return True, int(corrected_numbers[len(corrected_numbers) // 2])


def part_2():
    conditions = defaultdict(list)
    put_conditions = True
    outcome = 0
    for row in data:
        if row == "":
            put_conditions = False
            continue
        if put_conditions:
            before, after = row.split("|")
            conditions[before].append(after)
        else:
            is_ok, middle_number = check_row_with_conditions_part_2(row, conditions)
            if is_ok:
                outcome += middle_number
    print(outcome)


part_2()