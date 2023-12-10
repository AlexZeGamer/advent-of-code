# Advent of Code 2023 - Day 10
# https://adventofcode.com/2023/day/10
# Author: Alexandre MALFREYT

from visualisation import visu_color, visu_green, visu_BandW
from functions import *
import tests

VISU = True

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

maze = [[c for c in line] for line in lines]


if __name__ == '__main__':
    # Make a copy of the maze to avoid modifying the original
    maze = [line.copy() for line in maze]

    # Replace start with the correct pipe
    start = find_start(maze)
    maze[start[0]][start[1]] = predict_pipe(maze, start)

    # Part 1
    path = get_path(maze, start)
    print(f'Part 1 : {get_farthest_point_distance(path)}')

    # Part 2
    # print(f'Part 2 : {get_number_of_tiles_in_loop(maze, path)}')

    # Visualisation
    import time
    start = time.time()

    visu_color(maze, path, True) if VISU else None
    
    end = time.time()
    print(f'Visualisation time: {end-start} s')
    