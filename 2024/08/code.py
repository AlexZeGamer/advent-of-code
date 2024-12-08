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
                    antinodes[antinode] = []
                antinodes[antinode] += [type]

print(f'Part 1 : {len(antinodes.keys())}')


# Part 2
...
print(f'Part 2 : {...}')
