# Advent of Code 2023 - Day 5
# https://adventofcode.com/2023/day/5
# Author: Alexandre MALFREYT

from typing import List

DEBUG = False
VERBOSE = False

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

seeds = [int(seed) for seed in lines[0].split(' ')[1:]]

maps = []
i = -1
for line in lines[2:]:
    if line.endswith(':'):
        maps.append([])
        i += 1
    elif line != '':
        map_line = [int(l) for l in line.split(' ')]
        map_line[0], map_line[1] = map_line[1], map_line[0] # Swap source and destination ranges
        maps[i].append(map_line)

# from pprint import pprint
# pprint(maps) if DEBUG else None

# Sorting maps by source range start
for i in range(len(maps)):
    maps[i].sort(key=lambda x: x[0])

# Format:
"""
maps = [
    [
        ...
        [source range start, destination range start, range length],
        ...
    ],
    ...
]
"""

# Example:
# seeds = [79, 14, 55, 13]
# maps = [
#     [
#         [50, 52, 48],
#         [98, 50, 2],
#     ],
#     [
#         [0, 39, 15],
#         [15, 0, 37],
#         [52, 37, 2],
#     ],
#     [
#         [0, 42, 7],
#         [7, 57, 4],
#         [11, 0, 42],
#         [53, 49, 8],
#     ],
#     [
#         [18, 88, 7],
#         [25, 18, 70],
#     ],
#     [
#         [45, 81, 19],
#         [64, 68, 13],
#         [77, 45, 23],
#     ],
#     [
#         [0, 1, 69],
#         [69, 0, 1],
#     ],
#     [
#         [56, 60, 37],
#         [93, 56, 4],
#     ]
# ]

# Part 1
def find_appropriate_range_dicho(map: List[List[int]], value: int) -> List[int] or None:
    """Find the appropriate range for a value in a map using dichotomy"""
    min = 0
    max = len(map) - 1
    while True:
        i = (min + max) // 2

        # If we find a range, we return it
        if map[i][0] <= value < map[i][0] + map[i][2]:
            return map[i]
    
        # If we can't find a range, we return None
        elif min >= max:
            return None
        
        # else we continue the search
        elif map[i][0] > value:
            max = i - 1
        elif map[i][0] + map[i][2] <= value:
            min = i + 1

def a_to_b(value: int, map: List[List[int]]) -> int:
    """Get the destination of a value through a map"""
    range = find_appropriate_range_dicho(map, value)
    if range is None:
        dest = value
    else:
        dest = range[1] + (value - range[0])
    return dest

dests = seeds[:]
for i in range(len(seeds)):
    print(f'Seed {i+1} / {len(seeds)} : {seeds[i]}') if DEBUG and VERBOSE else None
    print(f'{seeds[i]}', end=' ') if DEBUG and not VERBOSE else None

    res = seeds[i]

    for j in range(len(maps)):
        print(f'Map {j+1} / {len(maps)} : {maps[j]}', end=' ') if DEBUG and VERBOSE else None

        res = a_to_b(res, maps[j])

        print(f'-> {res}') if DEBUG and VERBOSE else None
        print(f'{res}', end=' ') if DEBUG and not VERBOSE else None
    print() if DEBUG and not VERBOSE else None

    dests[i] = res

print(dests) if DEBUG else None

print(f'Part 1 : {min(dests)}')


# Part 2

dest = None

import time, humanize
print(seeds[1:10:2])
print(sum(seeds[1::2]))
done = 0
debut = time.time()
print_delta = 100000
for i in range(0, len(seeds), 2):
    seed_range = seeds[i]
    seed_range_length = seeds[i+1]
    print(f'Seed range {seed_range}') if DEBUG and VERBOSE else None

    for j in range(seed_range_length):
        done += 1
        print(f'{done} / {sum(seeds[1::2])}') if not done % print_delta else None
        print(f'Estimated total time : {humanize.naturaldelta((time.time() - debut) / done * sum(seeds[1::2]), minimum_unit="seconds")}') if not done % print_delta else None
        
        seed = seed_range + j
        print(f'Seed {seed}') if DEBUG and VERBOSE else None

        res = seed
        for map in maps:
            res = a_to_b(res, map)

        if dest is None or res < dest:
            dest = res

print(f'Part 2 : {dest}')
