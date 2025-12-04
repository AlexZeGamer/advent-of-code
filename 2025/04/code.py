# Advent of Code 2025 - Day 4
# https://adventofcode.com/2025/day/4
# Author: Alexandre MALFREYT

# Comment: Not my best code but it works and it's not too slow...

# Parse input
with open('input.txt', 'r') as f:
    grid = [[x for x in y.strip()] for y in f.readlines()]
    print(f'Grid size: {len(grid)} rows x {len(grid[0])} columns')


# Functions
def nb_accessible_paper_rolls(grid: list[list[str]], remove_rolls: bool = False) -> int:
    accessible_rolls = 0
    # for each cell in the grid
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] != "@": continue # skip non-paper roll cells
            
            # if less than 4 adjacent paper rolls, mark this one as accessible
            if nb_adjacent_paper_rolls(grid, (x, y)) < 4:
                accessible_rolls += 1
                if remove_rolls: grid[x][y] = "." # remove the roll from the grid
    return accessible_rolls

def nb_adjacent_paper_rolls(grid: list[list[str]], position: tuple[int, int]) -> int:
    x, y = position
    nb_adjacent_rolls = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0: continue # skip the current cell itself
            pos = (x+dx, y+dy)
            # check if the adjacent cell is within bounds
            if 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0]):
                # check if both cells are paper rolls
                if grid[pos[0]][pos[1]] == "@":
                    nb_adjacent_rolls += 1
    return nb_adjacent_rolls

def remove_accessible_paper_rolls(grid: list[list[str]], debug=False) -> int:
    """ Removes a maximum of one accessible paper roll from the grid and returns the number of rolls removed. """
    if debug:
        print("Initial state:")
        _print_grid(grid)
    
    total_removed = 0
    removed_this_round = -1
    while removed_this_round != 0:
        removed_this_round = nb_accessible_paper_rolls(grid, remove_rolls=True)
        total_removed += removed_this_round

        if debug and removed_this_round > 0:
            print(f"Remove {removed_this_round} roll of paper:")
            _print_grid(grid)
    return total_removed

def _print_grid(grid: list[list[str]]):
    for row in grid:
        print(''.join(row))
    print()

# Part 1 & 2
def part1(grid):
    return nb_accessible_paper_rolls(grid)

def part2(grid):
    return remove_accessible_paper_rolls(grid)


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
assert part2(grid_example) == 43


# Results
print(f'Part 1 : {part1(grid)}')
print(f'Part 2 : {part2(grid)}')
