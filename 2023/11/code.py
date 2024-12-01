# Advent of Code 2023 - Day 11
# https://adventofcode.com/2023/day/11
# Author: Alexandre MALFREYT

from typing import List, Tuple

DEBUG = False

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

image = [list(line) for line in lines]

# Example
# image = [
#     ['.','.','.','#','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','#','.','.'],
#     ['#','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','#','.','.','.'],
#     ['.','#','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','.','.','#'],
#     ['.','.','.','.','.','.','.','.','.','.'],
#     ['.','.','.','.','.','.','.','#','.','.'],
#     ['#','.','.','.','#','.','.','.','.','.'],
# ]

# Part 1
def expend_universe(universe: List[List[str]], expention: int = 2) -> List[List[str]]:
    """Expend the universe by duplicating the empty lines and columns"""
    universe = [line.copy() for line in universe]

    # Vertically
    i = 0
    while i < len(universe):
        if all([c == '.' for c in universe[i]]):
            # If the line is empty, duplicate it "expention" times
            for _ in range(expention-1):
                universe.insert(i, ['.'] * len(universe[i]))
            i += expention-1
        i += 1

    # Horizontally
    i = 0
    while i < len(universe[0]):
        is_empty = True
        for line in universe:
            if line[i] != '.':
                is_empty = False
                break

        # If the column is empty, duplicate it "expention" times
        if is_empty:
            for _ in range(expention-1):
                for line in universe:
                    line.insert(i, '.')
            i += expention-1
        i += 1

    return universe

def get_stars_location(universe: List[List[str]]) -> List[Tuple[int, int]]:
    """Get the location of the stars in the universe"""
    stars = []
    for i, line in enumerate(universe):
        for j, c in enumerate(line):
            if c == '#':
                stars.append((i, j))
    return stars

def vertical_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Return the vertical distance between two stars"""
    return abs(a[0] - b[0])

def horizontal_distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Return the horizontal distance between two stars"""
    return abs(a[1] - b[1])

def path(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Return the distance between two stars"""
    if a == b:
        return [a]
    
    # Vertical distance is smaller
    if vertical_distance(a, b) > horizontal_distance(a, b):
        # a is above b
        if a[0] < b[0]:
            # We go one step down
            return [(a[0], a[1])] + path((a[0] + 1, a[1]), b)
        # a is below b
        else:
            # We go one step up
            return [(a[0], a[1])] + path((a[0] - 1, a[1]), b)
    
    # Horizontal distance is smaller
    else:
        # a is on the left of b
        if a[1] < b[1]:
            # We go one step right
            return [(a[0], a[1])] + path((a[0], a[1] + 1), b)
        # a is on the right of b
        else:
            # We go one step left
            return [(a[0], a[1])] + path((a[0], a[1] - 1), b)

def print_universe(universe: List[List[str]], path: List[Tuple[int, int]] = None, show_ruler: bool = False) -> None:
    """Print the universe"""
    if show_ruler:
        print('  ', end='')
        for j in range(len(universe[0])):
            print(str(j)[:2] + ' ' * (2 - len(str(j))), end='')
        print()

    for i, line in enumerate(universe):
        print(str(i)[:2] + ' ' * (2 - len(str(i))), end='') if show_ruler else None
        
        for j, c in enumerate(line):
            if c == '#':
                print('██', end='')
            elif path is not None and (i, j) in path:
                print('▒▒', end='')
            elif c == '.':
                print('░░', end='')
        print()

def distance(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Return the distance between two stars"""
    return len(path(a, b)) - 1

universe = expend_universe(image)
stars = get_stars_location(universe)

total = 0
for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        total += distance(stars[i], stars[j])
        if DEBUG:
            print(f'{stars[i]} -> {stars[j]} : {distance(stars[i], stars[j])}')
            p = path(stars[i], stars[j])
            print_universe(universe, p, True)
            print()


print(f'Part 1 : {total}')


# Part 2
universe = expend_universe(image, 1_000_000)
stars = get_stars_location(universe)

total = 0
for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        total += distance(stars[i], stars[j])
        if DEBUG:
            print(f'{stars[i]} -> {stars[j]} : {distance(stars[i], stars[j])}')
            p = path(stars[i], stars[j])
            print_universe(universe, p, True)

print(f'Part 2 : {total}')
