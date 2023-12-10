# Advent of Code 2023 - Day 10
# https://adventofcode.com/2023/day/10
# Author: Alexandre MALFREYT

from time import sleep

from typing import List, Tuple

DEBUG = False
VISU = True

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

maze = [[c for c in line] for line in lines]

repr = {'|': '║', '-': '═', 'L': '╚', 'J': '╝', '7': '╗', 'F': '╔', '.': ' ', 'S': '█'}

# Part 1
example1 = [['-','L','|','F','7'], ['7','S','-','7','|'], ['L','|','7','|','|'], ['-','L','-','J','|'], ['L','|','-','J','F']]
example2 = [['7','-','F','7','-'], ['.','F','J','|','7'], ['S','J','L','L','7'], ['|','F','-','-','J'], ['L','J','.','L','J']]

def visu_color(maze: List[List[str]], path: List[Tuple[int, int]]) -> None:
    colors = ['\033[34m', '\033[94m', '\033[36m', '\033[96m', '\033[32m', '\033[92m', '\033[93m', '\033[33m', '\033[91m', '\033[31m', '\033[35m', '\033[95m']

    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            color = colors[int((path.index((i,j)) / len(path)) * len(colors))] if (i,j) in path else '\033[90m'
            print(color, end='')
            print(repr[c], end='')
            print('\033[0m', end='')
        print()

def visu_green(maze: List[List[str]], path: List[Tuple[int, int]]) -> None:
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            color = '\033[92m' if (i,j) in path else '\033[90m'
            print(color, end='')
            print(repr[c], end='')
            print('\033[0m', end='')
        print()

def visu_BandW(maze: List[List[str]], path: List[Tuple[int, int]]) -> None:
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            print(repr[c], end='')
        print()

def find_start(maze: List[List[str]]) -> Tuple[int, int]:
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            if c == 'S':
                return (i,j)
    
def is_connected(maze: List[List[str]], pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    # Same line (x)
    if pos1[0] == pos2[0]:
        possible_left = ['-', 'L', 'F', 'S']
        possible_right = ['-', 'J', '7', 'S']

        poses_sorted = sorted([pos1, pos2], key=lambda pos: pos[1])
        left, right = poses_sorted
        
        return maze[left[0]][left[1]] in possible_left and maze[right[0]][right[1]] in possible_right

    # Same column (y)
    if pos1[1] == pos2[1]:
        possible_up = ['|', 'F', '7', 'S']
        possible_down = ['|', 'J', 'L', 'S']

        poses_sorted = sorted([pos1, pos2], key=lambda pos: pos[0])
        up, down = poses_sorted
        
        return maze[up[0]][up[1]] in possible_up and maze[down[0]][down[1]] in possible_down
    
    # Not connected
    return False


def next_pos(maze: List[List[str]], pos: Tuple[int, int], prev: Tuple[int, int]) -> Tuple[int, int]:
    x, y = pos
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        # Same as previous
        if (x+dx, y+dy) == prev:
            continue
        
        # Out of bounds
        if x+dx < 0 or x+dx >= len(maze) or y+dy < 0 or y+dy >= len(maze[0]):
            continue

        if is_connected(maze, pos, (x+dx, y+dy)):
            return (x+dx, y+dy)

def get_path(maze: List[List[str]]) -> List[Tuple[int, int]]:
    start = find_start(maze)
    pos = start
    path = [start]
    visu_BandW(maze) if DEBUG else None
    while pos != start or len(path) <= 1:
        prev = path[-2] if len(path) > 1 else None
        pos = next_pos(maze, pos, prev)

        visu_color(maze, path) if DEBUG else None
        sleep(0.2) if DEBUG else None

        path.append(pos)
    visu_color(maze, path) if VISU else None
    return path

def get_farthest_point_distance(path: List[Tuple[int, int]]) -> int:
    return len(path)//2

example_paths = [get_path(e) for e in [example1, example2]]
path = get_path(maze)
print(f'Part 1 : {get_farthest_point_distance(path)}')


# Part 2
total = 0



print(f'Part 2 : {total}')
