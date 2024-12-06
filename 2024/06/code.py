# Advent of Code 2024 - Day 6
# https://adventofcode.com/2024/day/6
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    grid = [[x for x in y.strip()] for y in f.readlines()]

# grid = [
#     ['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '#'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '#', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '#', '.', '.', '^', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
#     ['#', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#     ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
# ]


# Part 1
def get_current_position_and_direction(grid):
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter == '^':
                return (x, y), 'NORTH'
            elif letter == '>':
                return (x, y), 'EAST'
            elif letter == 'v':
                return (x, y), 'SOUTH'
            elif letter == '<':
                return (x, y), 'WEST'
    raise ValueError('No starting position found')

def move_forward(position, direction):
    x, y = position
    if direction == 'NORTH':
        return (x, y - 1)
    elif direction == 'EAST':
        return (x + 1, y)
    elif direction == 'SOUTH':
        return (x, y + 1)
    elif direction == 'WEST':
        return (x - 1, y)

def turn_right(direction):
    if direction == 'NORTH':
        return 'EAST'
    elif direction == 'EAST':
        return 'SOUTH'
    elif direction == 'SOUTH':
        return 'WEST'
    elif direction == 'WEST':
        return 'NORTH'

def print_grid(grid):
    print('\n'.join([''.join(x) for x in grid]))
    print()

def get_path(_grid, do_print_grid=False):
    grid = [line.copy() for line in _grid]

    visited = []
    (x, y), direction = get_current_position_and_direction(grid)

    while True:
        if not len(visited) or visited[-1] != (x, y):
            grid[y][x] = 'X'
            visited.append((x, y))

        new_x, new_y = move_forward((x, y), direction)
        if new_x < 0 or new_x >= len(grid[0]) or new_y < 0 or new_y >= len(grid):
            break

        if grid[new_y][new_x] in ['#', 'O']:
            direction = turn_right(direction)
        else:
            # If (x, y) and (new_x, new_y) are in visited next to each other in the same order, we have a loop
            # for i in range(len(visited) - 1):
            #     if visited[i] == (x, y) and visited[i + 1] == (new_x, new_y):
            #         grid[y][x] = 'L'
            #         raise ValueError('Loop detected')
            if len(visited) >= 10000:
                raise ValueError('Loop detected')
            x, y = new_x, new_y

    if do_print_grid:
        print_grid(grid)

    return set(visited)

def get_path_length(grid):
    visited = get_path(grid)
    return len(set(visited))

print(f'Part 1 : {get_path_length(grid)}')


# Part 2
possible_obstructions = []

import itertools
i = 0
start_position, _ = get_current_position_and_direction(grid)

# get every cell next to the path (max 1 cell away) or on the path
path = get_path(grid)
to_test = []
for x, y in itertools.product(range(len(grid[0])), range(len(grid))):
    if (x, y) in path or any(abs(x - x2) <= 1 and abs(y - y2) <= 1 for (x2, y2) in path):
        to_test.append((x, y))

# for x, y in itertools.product(range(len(grid[0])), range(len(grid))):
for x, y in to_test:
    i += 1
    # print(f'{i}/{len(grid) * len(grid[0])}', end='\r')
    print(f'{i}/{len(to_test)}', end='\r') if i % 100 == 0 else None
    
    if grid[y][x] == '#' or (x, y) == start_position:
        continue

    grid_with_obstacle = [line.copy() for line in grid]
    grid_with_obstacle[y][x] = 'O'
    try:
        get_path_length(grid_with_obstacle)
    except ValueError as e:
        if 'Loop detected' in str(e):
            possible_obstructions.append((x, y))

print(f'Part 2 : {len(possible_obstructions)}')
