from itertools import product 

with open("day7/input.txt", "r") as f:
    data = f.read().splitlines()


equations = []
for row in data:
    parts = row.split(":")
    outcome = int(parts[0])
    numbers = [int(number) for number in parts[1].split(" ")[1:]]
    equations.append((outcome, numbers))



def find_equation(equation: tuple[int, list[int]]) -> bool:
    outcome, numbers = equation
    combinations = list(product(["+", "*"], repeat=len(numbers)))
    combination_outcome = 0
    for combination in combinations:
        for i in range(len(combination)):
            if combination[i] == "+":
                combination_outcome += numbers[i]
            else:
                combination_outcome *= numbers[i]
        if combination_outcome == outcome:
            return True
        combination_outcome = 0
    return False

outcome = 0
for equation in equations:
    if find_equation(equation):
        outcome += equation[0]
print(outcome)
