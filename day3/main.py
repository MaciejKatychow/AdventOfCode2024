import re

with open("day3/input.txt", "r") as f:
    data = f.read().splitlines()


def calculate_mul(mul: str) -> int:
    digits = re.findall(r'\d+', mul)
    a = int(digits[0]) * int(digits[1])
    return a

outcome = 0
for row in data:
    good_muls = re.findall(r'mul\(\d+,\d+\)', row)
    for mul in good_muls:
        outcome += calculate_mul(mul)
print(outcome)