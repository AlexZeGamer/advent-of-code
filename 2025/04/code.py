# Advent of Code 2025 - Day 4
# https://adventofcode.com/2025/day/4
# Author: Alexandre MALFREYT

# Parse input
with open('input.txt', 'r') as f:
    grid = [[x for x in y.strip()] for y in f.readlines()]
    print(f'Grid size: {len(grid)} rows x {len(grid[0])} columns')


# Functions
def nb_accessible_paper_rolls(grid: list[list[str]]) -> int:
    accessible_rolls = 0
    # for each cell in the grid
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != "@": continue # skip non-paper roll cells
            
            nb_adjacent_rolls = 0
            # for each adjacent cell (including diagonals)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0: continue # skip the current cell itself
                    pos = (x+dx, y+dy)
                    # check if the adjacent cell is within bounds
                    if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                        # check if both cells are paper rolls
                        if grid[x][y] == "@" and grid[pos[0]][pos[1]] == "@":
                            nb_adjacent_rolls += 1
            # if less than 4 adjacent paper rolls, mark this one as accessible
            if nb_adjacent_rolls < 4:
                accessible_rolls += 1
    return accessible_rolls
                    

# Part 1 & 2
def part1(grid):
    return nb_accessible_paper_rolls(grid)

def part2(grid):
    ...


# Tests
grid_example = [
    [".",".","@","@",".","@","@","@","@","."],
    ["@","@","@",".","@",".","@",".","@","@"],
    ["@","@","@","@","@",".","@",".","@","@"],
    ["@",".","@","@","@","@",".",".","@","."],
    ["@","@",".","@","@","@","@",".","@","@"],
    [".","@","@","@","@","@","@","@",".","@"],
    [".","@",".","@",".","@",".","@","@","@"],
    ["@",".","@","@","@",".","@","@","@","@"],
    [".","@","@","@","@","@","@","@","@","."],
    ["@",".","@",".","@","@","@",".","@","."],
]

assert part1(grid_example) == 13
# assert part2(grid_example) == ...


# Results
print(f'Part 1 : {part1(grid)}')
print(f'Part 2 : {part2(grid)}')