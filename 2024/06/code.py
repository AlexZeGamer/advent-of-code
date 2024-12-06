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

def get_symbol_for_direction(direction):
    if direction == 'NORTH':
        return '^'
    elif direction == 'EAST':
        return '>'
    elif direction == 'SOUTH':
        return 'v'
    elif direction == 'WEST':
        return '<'

total = 1
visited = set()
(x, y), direction = get_current_position_and_direction(grid)
while True:
    new_x, new_y = move_forward((x, y), direction)
    try:
        if grid[new_y][new_x] == '#':
            direction = turn_right(direction)
        else:
            grid[y][x] = 'X'
            visited.add((x, y))
            if not (new_x, new_y) in visited:
                total += 1

            grid[new_y][new_x] = get_symbol_for_direction(direction)
            x, y = new_x, new_y
    except IndexError:
        break

# print('\n'.join([''.join(x) for x in grid]))

print(f'Part 1 : {total}')


# Part 2



print(f'Part 2 : {total}')
