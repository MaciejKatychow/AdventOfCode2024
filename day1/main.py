with open ('day1/input.txt') as f:
    data = f.read().splitlines()


list_1 = []
list_2 = []
for row in data:
    parts = row.split(" ")
    list_1.append(int(parts[0]))
    list_2.append(int(parts[-1]))


def part_1(list_1, list_2):
    sorted_list_1 = sorted(list_1)
    sorted_list_2 = sorted(list_2)

    outcome = 0
    for i in range(len(sorted_list_1)):
        outcome += abs(sorted_list_1[i] - sorted_list_2[i])

    print(outcome)

outcome = 0

for x in list_1:
    outcome += x * list_2.count(x)
print(outcome)
