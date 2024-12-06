with open("day6/input.txt", "r") as f:
    data = f.read().splitlines()

for i in range(len(data)):
    data[i] = list(data[i])


GOURD_PATH = [(-1,0), (0,1), (1,0), (0,-1)]


ROW_LENGTH = len(data[0])
for row in data:
    if len(row) != ROW_LENGTH:
       raise ValueError("All rows must have the same length") 

start_i = None
start_j = None
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            start_i = i
            start_j = j
            break
    if start_i is not None:
        break

outcome = 1
i = start_i
j = start_j
data[i][j] = "X"
current_index = 0
current_direction = GOURD_PATH[current_index]
while True:
    i += current_direction[0]
    j += current_direction[1]
    if i >= len(data) or j >= len(data[i]) or i < 0 or j < 0:
        break

    if data[i][j] == "#":
        i -= current_direction[0]
        j -= current_direction[1]
        current_index += 1
        next_index = (current_index) % len(GOURD_PATH)
        current_direction = GOURD_PATH[next_index]
    elif data[i][j] == ".":
        outcome += 1
        data[i][j] = "X"

print(outcome)
