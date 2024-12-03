import re

with open("day3/input.txt", "r") as f:
    data = f.read().splitlines()


def calculate_mul(mul: str) -> int:
    digits = re.findall(r'\d+', mul)
    a = int(digits[0]) * int(digits[1])
    return a

outcome = 0
count_do = 0
count_dont = 0
do = True
for row in data:
    good_muls = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', row)
    count_do += good_muls.count("do()")
    count_dont += good_muls.count("don't()")
    for index, mul in enumerate(good_muls):
        if mul == "do()":
            do = True
        elif mul == "don't()":
            do = False
        else:
            if do:
                digits = re.findall(r'\d+', mul)
                outcome += int(digits[0]) * int(digits[1])
print(outcome)