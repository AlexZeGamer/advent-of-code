# Advent of Code 2024 - Day 12
# https://adventofcode.com/2024/day/12
# Author: Alexandre MALFREYT

# Parse input
with open('input.txt', 'r') as f:
    text = f.read() # For text input
    # lines = f.readlines() # For line input
    # grid = [[x for x in y.strip()] for y in f.readlines()] # For grid input

# Functions
...

# Part 1 & 2
def part1(map):
    ...

def part2(map):
    ...

# Tests
map_example1 = [
    ['A','A','A','A'],
    ['B','B','C','D'],
    ['B','B','C','C'],
    ['E','E','E','C'],
]

assert part1(map_example1) == 140

map_example2 = [
    ['O','O','O','O','O'],
    ['O','X','O','X','O'],
    ['O','O','O','O','O'],
    ['O','X','O','X','O'],
    ['O','O','O','O','O'],
]

assert part1(map_example2) == 772

map_example3 = [
    ['R','R','R','R','I','I','C','C','F','F'],
    ['R','R','R','R','I','I','C','C','C','F'],
    ['V','V','R','R','R','C','C','F','F','F'],
    ['V','V','R','C','C','C','J','F','F','F'],
    ['V','V','V','V','C','J','J','C','F','E'],
    ['V','V','I','V','C','C','J','J','E','E'],
    ['V','V','I','I','I','C','J','J','E','E'],
    ['M','I','I','I','I','I','J','J','E','E'],
    ['M','I','I','I','S','I','J','E','E','E'],
    ['M','M','M','I','S','S','J','E','E','E'],
]

assert part1(map_example3) == 1930

# Results
print(f'Part 1 : {total}')
print(f'Part 2 : {total}')
