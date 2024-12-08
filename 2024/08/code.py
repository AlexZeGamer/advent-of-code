# Advent of Code 2024 - Day 8
# https://adventofcode.com/2024/day/8
# Author: Alexandre MALFREYT

import itertools

with open('input.txt', 'r') as f:
    grid = [[x for x in y.strip()] for y in f.readlines()]

# Example
# grid = [
#     ['.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','0','.','.','.'],
#     ['.','.','.','.','.','0','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','0','.','.','.','.'],
#     ['.','.','.','.','0','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','A','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','A','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','A','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.','.','.'],
# ]

DEBUG = False

# Part 1
def get_antennas(grid: list[list[str]]) -> dict[str, list[tuple[int, int]]]:
    """
    Return a dictionary of antennas with their positions
    Example: {'A': [(0, 0), (1, 0)], 'B': [(3, 2)]}
    """
    antennas = {}
    for x, y in itertools.product(range(len(grid[0])), range(len(grid))):
        if grid[y][x] != '.':
            if grid[y][x] not in antennas:
                antennas[grid[y][x]] = []
            antennas[grid[y][x]].append((x, y))

    return antennas

def get_antinodes(a: tuple[int, int], b: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """
    Return the 2 antinodes of two antennas

    Examples:
        ((8, 1), (5, 2)) => ((11, 0), (2, 3))
        ((5, 2), (7, 3)) => ((3, 1), (9, 4))
    """
    x_diff = a[0] - b[0]
    y_diff = a[1] - b[1]
    return (
        (a[0] + x_diff, a[1] + y_diff),
        (b[0] - x_diff, b[1] - y_diff)
    )

def check_antinode(antinode: tuple[int, int], grid: list[list[str]]) -> bool:
    """
    Return True if the antinode is in the grid
    """
    return 0 <= antinode[0] < len(grid[0]) and 0 <= antinode[1] < len(grid)

def print_grid_with_antinodes(grid: list[list[str]], antinodes: dict[tuple[int, int], list[str]]):
    """
    Print the grid with the antinodes
    """
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (x, y) in antinodes:
                print('\033[1;37;40m#\033[0m', end='')
            else:
                print(grid[y][x], end='')
        print()

assert set(get_antinodes((8, 1), (5, 2))) == set(((11, 0), (2, 3)))
assert set(get_antinodes((5, 2), (7, 3))) == set(((3, 1), (9, 4)))
assert set(get_antinodes((5, 2), (8, 1))) == set(((11, 0), (2, 3)))
assert set(get_antinodes((7, 3), (5, 2))) == set(((3, 1), (9, 4)))

antinodes = {}
for type, positions in get_antennas(grid).items():
    for comb in itertools.combinations(positions, 2):
        # antinodes[type] += [antinode for antinode in get_antinodes(*comb) if check_antinode(antinode, grid)]
        for antinode in get_antinodes(*comb):
            if check_antinode(antinode, grid):
                if antinode not in antinodes:
                    antinodes[antinode] = set()
                antinodes[antinode].add(type)

print_grid_with_antinodes(grid, antinodes) if DEBUG else None
print(f'Part 1 : {len(antinodes.keys())}')


# Part 2
def get_antinodes_with_resonant_harmonics(a: tuple[int, int], b: tuple[int, int], grid: list[list[str]]) -> tuple[tuple[int, int], ...]:
    """
    Return all the antinodes of two antennas with resonant harmonics
    """
    x_diff = a[0] - b[0]
    y_diff = a[1] - b[1]
    
    i = 1
    antinodes = []
    antinodes.append(a)
    antinodes.append(b)
    while True:
        continue_loop = False

        # get every antinode in the positive direction (by adding x_diff and y_diff)
        antinode_positive = (a[0] + x_diff * i, a[1] + y_diff * i)
        if check_antinode(antinode_positive, grid):
            antinodes.append(antinode_positive)
            continue_loop = True

        # get every antinode in the negative direction (by substracting x_diff and y_diff)
        antinode_negative = (b[0] - x_diff * i, b[1] - y_diff * i)
        if check_antinode(antinode_negative, grid):
            antinodes.append(antinode_negative)
            continue_loop = True

        i += 1
        if not continue_loop:
            break

    return tuple(antinodes)

antinodes_with_resonant_harmonics = {}
for type, positions in get_antennas(grid).items():
    for comb in itertools.combinations(positions, 2):
        for antinode in get_antinodes_with_resonant_harmonics(*comb, grid):
            if antinode not in antinodes_with_resonant_harmonics:
                antinodes_with_resonant_harmonics[antinode] = set()
            antinodes_with_resonant_harmonics[antinode].add(type)

print_grid_with_antinodes(grid, antinodes_with_resonant_harmonics) if DEBUG else None

print(f'Part 2 : {len(antinodes_with_resonant_harmonics.keys())}')
