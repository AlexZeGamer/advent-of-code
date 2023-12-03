# Advent of Code 2023 - Day 3
# https://adventofcode.com/2023/day/3
# Author: Alexandre MALFREYT

from typing import List

DEBUG = True

with open('input.txt', 'r') as f:
    engine_schematic = [line.strip() for line in f.readlines()]

# Example
# engine_schematic = [
#     '467..114..',
#     '...*......',
#     '..35..633.',
#     '......#...',
#     '617*......',
#     '.....+.58.',
#     '..592.....',
#     '......755.',
#     '...$.*....',
#     '.664.598..',
# ]

# Part 1
total = 0

def is_number(char):
    return '0' <= char <= '9'

def is_empty(char):
    return char == '.'

def is_symbol(char):
    return not is_number(char) and not is_empty(char)

def has_symbol_adjacent(x, y, engine_schematic):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0 or i >= len(engine_schematic) or j >= len(engine_schematic[0]):
                continue
            if is_symbol(engine_schematic[i][j]):
                return True
    return False

def is_part_number(x, y_begin, y_end, engine_schematic):
    y = y_begin
    while y < len(engine_schematic[x]) and is_number(engine_schematic[x][y]):
        if has_symbol_adjacent(x, y, engine_schematic):
            return True
        y += 1
    return False

current_number = ''
for i in range(len(engine_schematic)):
    print() if DEBUG else None
    for j in range(len(engine_schematic[i])):
        if is_empty(engine_schematic[i][j]):
            print('\033[90m' + engine_schematic[i][j] + '\033[0m', end='') if DEBUG else None # dark grey
            continue
        if is_symbol(engine_schematic[i][j]):
            print('\033[37m' + engine_schematic[i][j] + '\033[0m', end='') if DEBUG else None # light grey
            continue

        # if this is the beginning of a number
        if j == 0 or not is_number(engine_schematic[i][j-1]):
            current_number = ''
            j_begin = j

        j_end = j
        current_number += engine_schematic[i][j]

        # if this is the end of a number
        if j == len(engine_schematic[i])-1 or not is_number(engine_schematic[i][j+1]):
            if current_number != '':
                if is_part_number(i, j_begin, j_end, engine_schematic):
                    print('\033[92m' + current_number + '\033[0m', end='') if DEBUG else None # green
                    total += int(current_number)
                else:
                    print('\033[91m' + current_number + '\033[0m', end='') if DEBUG else None # red
                current_number = ''
print() if DEBUG else None

print(f'Part 1 : {total}')

# Part 2
total = 0

def is_gear(char):
    return char == '*'

def get_numbers_adjacent(x, y, engine_schematic) -> List[int]:
    numbers = []
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i < 0 or j < 0 or i >= len(engine_schematic) or j >= len(engine_schematic[0]):
                continue
            if is_number(engine_schematic[i][j]):
                numbers.append(get_number(i, j, engine_schematic))
    return set(numbers) # remove duplicates

def get_number(x, y, engine_schematic) -> int:
    y_begin = y
    y_end = y
    while y_begin > 0 and is_number(engine_schematic[x][y_begin-1]):
        y_begin -= 1
    while y_end < len(engine_schematic[x])-1 and is_number(engine_schematic[x][y_end+1]):
        y_end += 1
    return int(engine_schematic[x][y_begin:y_end+1])

for i in range(len(engine_schematic)):
    for j in range(len(engine_schematic[i])):
        if is_gear(engine_schematic[i][j]):
            print('Gear at', i, j, 'with numbers', get_numbers_adjacent(i, j, engine_schematic)) if DEBUG else None
            numbers = get_numbers_adjacent(i, j, engine_schematic)
            if len(numbers) >= 2:
                sub_total = 1
                for number in numbers:
                    sub_total *= number
                total += sub_total

print(f'Part 2 : {total}')
