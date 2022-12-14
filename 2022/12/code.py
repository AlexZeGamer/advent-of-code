# Advent of Code 2022 - Day 12
# https://adventofcode.com/2022/day/12
# Author: Alexandre MALFREYT
from typing import List, Tuple
import sys

# sys.setrecursionlimit(10000)

with open('input.txt', 'r') as f:
    map = f.read().splitlines()

# map = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# """.splitlines()

#########
#  -> y #
# ↓     #
# x     #
#########

def get_height(coords: Tuple[int, int]) -> str:
    if map[coords[0]][coords[1]] == 'S':
        return 'a'
    if map[coords[0]][coords[1]] == 'E':
        return 'z'
    return map[coords[0]][coords[1]]

def distance_to_end(
    coords: Tuple[int, int],
    visited: List[Tuple[int, int]] = [],
) -> int:
    x = coords[0]
    y = coords[1]
    current_height = map[x][y]
    if current_height == 'S':
        current_height = 'a'
    if current_height == 'E':
        print('end')
        return len(visited)

    # print(len(visited), end='\r')
    # print(visited)

    distances = []

    # Go up
    if x != 0 and not (x - 1, y) in visited:
        if ord(current_height) in range(ord(get_height((x-1, y)))-1, ord(get_height((x-1, y)))+2):
            # print('up')
            sub_distance = distance_to_end((x - 1, y), visited + [(x - 1, y)])
            if sub_distance:
                distances.append(sub_distance)
    
    # Go down
    if x != len(map) - 1 and not (x + 1, y) in visited:
        if ord(current_height) in range(ord(get_height((x+1, y)))-1, ord(get_height((x+1, y)))+2):
            # print('down')
            sub_distance = distance_to_end((x + 1, y), visited + [(x + 1, y)])
            if sub_distance:
                distances.append(sub_distance)
    
    # Go left
    if y != 0 and not (x, y - 1) in visited:
        if ord(current_height) in range(ord(get_height((x, y-1)))-1, ord(get_height((x, y-1)))+2):
            # print('left')
            sub_distance = distance_to_end((x, y - 1), visited + [(x, y - 1)])
            if sub_distance:
                distances.append(sub_distance)

    # Go right
    if y != len(map[0]) - 1 and not (x, y + 1) in visited:
        if ord(current_height) in range(ord(get_height((x, y+1)))-1, ord(get_height((x, y+1)))+2):
            # print('right')
            sub_distance = distance_to_end((x, y + 1), visited + [(x, y + 1)])
            if sub_distance:
                distances.append(sub_distance)

    if not len(distances):
        return 0
    
    print([d for d in distances if d is not None])
    return min([d for d in distances if d is not None])

print('début')
print(distance_to_end((20, 0), [(20, 0)]))
print('fini')



# Part 1
total = 0



print(f'Part 1 : {total}')


# Part 2
total = 0



print(f'Part 2 : {total}')
