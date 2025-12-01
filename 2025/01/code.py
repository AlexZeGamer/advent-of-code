# Advent of Code 2025 - Day 1
# https://adventofcode.com/2025/day/1
# Author: Alexandre MALFREYT

from typing import Literal

# Parse input
with open('input.txt', 'r') as f:
    lines = f.readlines()


# Functions
def unlock_safe(
    combination: list[str],
    method: Literal["ends", "clicks"] = "clicks",
    start=50,
):
    nb_zero = 0
    position = start
    for line in combination:
        direction, nb_steps = line[0], int(line[1:])

        if method == "ends":
            position += nb_steps if direction=="R" else -nb_steps
            position %= 100
            if position == 0: nb_zero+=1
        
        if method == "clicks":
            for _ in range(nb_steps):
                position += 1 if direction=="R" else -1
                position %= 100
                if position == 0: nb_zero+=1

    return nb_zero


# Part 1 & 2
def part1(lines):
    return unlock_safe(lines, method="ends")

def part2(lines):
    return unlock_safe(lines, method="clicks")

# Tests
lines_example = [ "L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82" ]
assert part1(lines_example) == 3
assert part2(lines_example) == 6

# Results
print(f'Part 1 : {part1(lines)}')
print(f'Part 2 : {part2(lines)}')
