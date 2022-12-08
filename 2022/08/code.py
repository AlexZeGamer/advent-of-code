# Advent of Code 2022 - Day 8
# https://adventofcode.com/2022/day/8
# Author: Alexandre MALFREYT
from typing import List

with open('input.txt', 'r') as f:
    forest = f.read().split('\n')[:-1]

forest = [[int(tree) for tree in line] for line in forest]

height = len(forest)
width = len(forest[0])


# Part 1
def is_visible(forest: List[List[int]], x: int, y: int) -> bool:
    height = len(forest)
    width = len(forest[0])


    visible_bottom = all(
        forest[i][y] < forest[x][y]
        for i in range(x+1, height)
    )
    
    visible_top = all(
        forest[i][y] < forest[x][y]
        for i in range(x-1, -1, -1)
    )
    
    visible_right = all(
        forest[x][j] < forest[x][y]
        for j in range(y+1, width)
    )
    
    visible_left = all(
        forest[x][j] < forest[x][y]
        for j in range(y-1, -1, -1)
    )

    visible = any([visible_bottom, visible_top, visible_right, visible_left])

    return visible
    

# All trees on the border are visible, so we can remove them from the count
total = 2*(height + width) - 4

for x in range(1, height-1):
    for y in range(1, width-1):
        if is_visible(forest, x, y):
            total += 1

print(f'Part 1 : {total}')


# Part 2
def scenic_score(forest: List[List[int]], x:int, y: int) -> int:
    height = len(forest)
    width = len(forest[0])
    
    # bottom
    for i in range(x+1, height):
        if forest[i][y] >= forest[x][y]:
            distance_bottom = i - x
            break
    else:
        distance_bottom = height - x - 1
    
    # top
    for i in range(x-1, -1, -1):
        if forest[i][y] >= forest[x][y]:
            distance_top = x - i
            break
    else:
        distance_top = x
    
    # right
    for j in range(y+1, width):
        if forest[x][j] >= forest[x][y]:
            distance_right = j - y
            break
    else:
        distance_right = width - y - 1
    
    # left
    for j in range(y-1, -1, -1):
        if forest[x][j] >= forest[x][y]:
            distance_left = y - j
            break
    else:
        distance_left = y
    
    return distance_left * distance_right * distance_top * distance_bottom

sc_max = 0
for x in range(0, height):
    for y in range(0, width):
        sc = scenic_score(forest, x, y)
        sc_max = sc if sc > sc_max else sc_max

print(f'Part 2 : {sc_max}')
