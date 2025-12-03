# Advent of Code 2025 - Day 3
# https://adventofcode.com/2025/day/3
# Author: Alexandre MALFREYT

# Parse input
with open('input.txt', 'r') as f:
    battery_banks = [[int(x) for x in y.strip()] for y in f.readlines()]


# Functions
# https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
_max_idx = lambda lst: max(range(len(lst)), key=lst.__getitem__)

def find_highest_joltage(battery_bank: list[int]) -> int:
    # first digit: find the battery with the highest joltage (except the last one)
    first_digit_idx = _max_idx(battery_bank[:-1])
    first_digit = battery_bank[first_digit_idx]
    # second digit: get the highest joltage of the batteries after the highest one
    second_digit = max(battery_bank[first_digit_idx + 1:])
    return first_digit*10 + second_digit


# Part 1 & 2
def part1(battery_banks: list[list[int]]) -> int:
    total = 0
    for battery_bank in battery_banks:
        total += find_highest_joltage(battery_bank)
    return total

def part2(battery_banks: list[list[int]]) -> int:
    ...


# Tests
example = [
    [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
    [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
    [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1],
]

assert part1(example) == 357
# assert part2(example) == ...


# Results
print(f'Part 1 : {part1(battery_banks)}')
# print(f'Part 2 : {part2(battery_banks)}')