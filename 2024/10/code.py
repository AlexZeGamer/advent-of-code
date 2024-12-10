# Advent of Code 2024 - Day 10
# https://adventofcode.com/2024/day/10
# Author: Alexandre MALFREYT

import numpy as np

with open('input.txt', 'r') as f:
    map = [[int(x) for x in y.strip()] for y in f.readlines()]

# Example
# map = [
#     [8, 9, 0, 1, 0, 1, 2, 3],
#     [7, 8, 1, 2, 1, 8, 7, 4],
#     [8, 7, 4, 3, 0, 9, 6, 5],
#     [9, 6, 5, 4, 9, 8, 7, 4],
#     [4, 5, 6, 7, 8, 9, 0, 3],
#     [3, 2, 0, 1, 9, 0, 1, 2],
#     [0, 1, 3, 2, 9, 8, 0, 1],
#     [1, 0, 4, 5, 6, 7, 3, 2],
# ]

def get_score(map, trailhead, visited=None, check_visited=True):
    """
    Get the number of accessible cells with value 9 from a trailhead recursively
    """
    if visited is None:
        visited = set()

    x, y = trailhead
    current_value = map[x][y]
    if current_value == 9:
        return 1
    
    score = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x, new_y = x + dx, y + dy

        # Position out of bounds
        if new_x < 0 or new_x >= len(map) or new_y < 0 or new_y >= len(map[0]):
            continue

        # Position not accessible from current cell
        if map[new_x][new_y] != current_value + 1:
            continue

        # Position already visited
        if (new_x, new_y) in visited:
            continue

        visited.add((new_x, new_y)) if check_visited else None
        score += get_score(map, (new_x, new_y), visited if check_visited else None, check_visited)

    return score


# Part 1
total = 0

for (x, y), value in np.ndenumerate(map):
    if value == 0:
        total += get_score(map, (x, y), check_visited=True)

print(f'Part 1 : {total}')


# Part 2
total = 0

for (x, y), value in np.ndenumerate(map):
    if value == 0:
        total += get_score(map, (x, y), check_visited=False)

print(f'Part 2 : {total}')
