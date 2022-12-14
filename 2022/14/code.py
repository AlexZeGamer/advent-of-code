# Advent of Code 2022 - Day 14
# https://adventofcode.com/2022/day/14
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

lines = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines()

#########
#  -> x #
# ↓     #
# y     #
#########


# Find the min and max coordinates for visualization
min_x = max_x = int(lines[0].split(" -> ")[0].split(",")[0])
max_y = int(lines[0].split(" -> ")[0].split(",")[1])
min_y = 0 # We always start at the top
for line in lines:
    for coords in line.split(" -> "):
        x = int(coords.split(",")[0])
        y = int(coords.split(",")[1])
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

size_x = max_x - min_x + 1
size_y = max_y - min_y + 1

def show_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end='')
        print()

# Create an empty grid of . (air)
grid = [['.'] * size_x for _ in range(size_y)]

for line in lines:
    # Show the starting point with a +
    x = 500 - min_x
    y =   0 - min_y
    grid[y][x] = '+'


    # Fill the grid with a # for each wall
    for i in range(len(line.split(" -> ")) - 1):
        x1 = int(line.split(" -> ")[i].split(",")[0]) - min_x
        y1 = int(line.split(" -> ")[i].split(",")[1]) - min_y
        x2 = int(line.split(" -> ")[i + 1].split(",")[0]) - min_x
        y2 = int(line.split(" -> ")[i + 1].split(",")[1]) - min_y
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x1] = '#'
        else:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[y1][x] = '#'

show_grid(grid)

# Part 1
total = 0

# TODO: Sand simulation

print(f'Part 1 : {total}')


# Part 2
total = 0



print(f'Part 2 : {total}')
