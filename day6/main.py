from typing import Tuple


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


def part_1(start_i: int, start_j: int):
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
            next_index = current_index % len(GOURD_PATH)
            current_direction = GOURD_PATH[next_index]
        elif data[i][j] == ".":
            outcome += 1
            data[i][j] = "X"

    print(outcome)


def check_if_can_escape(data, current_index: int, current_direction: Tuple[int, int], i: int, j: int):
    visited_obstacles = []
    while True:
        i += current_direction[0]
        j += current_direction[1]
        if i >= len(data) or j >= len(data[i]) or i < 0 or j < 0:
            escaped = True
            break
    

        if data[i][j] == "#":
            obstacle = (i, j, current_direction)
            visited_obstacles.append(obstacle)
            if len(visited_obstacles) > 1:
                if obstacle in visited_obstacles[:-1]:
                    escaped = False
                    break

            i -= current_direction[0]
            j -= current_direction[1]
            current_index += 1
            next_index = current_index % len(GOURD_PATH)
            current_direction = GOURD_PATH[next_index]

    #Logic to check if gourd is stuck

    return escaped


def part_2(start_i: int, start_j: int):
    i = start_i
    j = start_j
    data[i][j] = "."
    current_index = 0
    current_direction = GOURD_PATH[current_index]
    visited_obstacles = []
    outcome_obstacles = []
    tried_obstacles = []
    escaped = False
    while True:
        obstacle_i = i + current_direction[0]
        obstacle_j = j + current_direction[1]
        try:
            data[obstacle_i][obstacle_j]
        except IndexError:
            break
        obstacle = (obstacle_i, obstacle_j)
        if data[obstacle_i][obstacle_j] == "." and  not obstacle in tried_obstacles:
            data[obstacle_i][obstacle_j] = "#"
            escaped = check_if_can_escape(data, current_index, current_direction, i, j)
            if not escaped:
                print(obstacle)
                outcome_obstacles.append(obstacle)
            
            tried_obstacles.append(obstacle)
            data[obstacle_i][obstacle_j] = "."
        
        i += current_direction[0]
        j += current_direction[1]

        if i >= len(data) or j >= len(data[i]) or i < 0 or j < 0:
            break

        if data[i][j] == "#":
            visited_obstacles.append((i,j, current_index))
            i -= current_direction[0]
            j -= current_direction[1]
            current_index += 1
            next_index = current_index % len(GOURD_PATH)
            current_direction = GOURD_PATH[next_index]

    print(len(outcome_obstacles))

part_2(start_i, start_j)