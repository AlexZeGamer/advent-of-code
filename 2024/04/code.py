# Advent of Code 2024 - Day 4
# https://adventofcode.com/2024/day/4
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    grid = [[letter for letter in line.strip()] for line in f.readlines()]

# grid = [
#     ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
#     ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
#     ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
#     ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
#     ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
#     ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
#     ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
#     ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
#     ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
#     ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X'],
# ]

# Part 1
total = 0

# get the position of every 'X' in the grid
x_pos_list = [(x, y) for y, row in enumerate(grid) for x, letter in enumerate(row) if letter == 'X']

for x, y in x_pos_list:
    word = 'XMAS'

    # check right
    if x + len(word) <= len(grid):
        if all(grid[y][x + i] == word[i] for i in range(len(word))):
            total += 1

    # check down
    if y + len(word) <= len(grid):
        if all(grid[y + i][x] == word[i] for i in range(len(word))):
            total += 1

    # check left
    if x - len(word) >= -1:
        if all(grid[y][x - i] == word[i] for i in range(len(word))):
            total += 1

    # check up
    if y - len(word) >= -1:
        if all(grid[y - i][x] == word[i] for i in range(len(word))):
            total += 1

    # check right-down
    if x + len(word) <= len(grid) and y + len(word) <= len(grid):
        if all(grid[y + i][x + i] == word[i] for i in range(len(word))):
            total += 1

    # check left-down
    if x - len(word) >= -1 and y + len(word) <= len(grid):
        if all(grid[y + i][x - i] == word[i] for i in range(len(word))):
            total += 1

    # check left-up
    if x - len(word) >= -1 and y - len(word) >= -1:
        if all(grid[y - i][x - i] == word[i] for i in range(len(word))):
            total += 1

    # check right-up
    if x + len(word) <= len(grid) and y - len(word) >= -1:
        if all(grid[y - i][x + i] == word[i] for i in range(len(word))):
            total += 1

print(f'Part 1 : {total}')


# Part 2
total = 0


print(f'Part 2 : {total}')
