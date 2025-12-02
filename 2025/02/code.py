# Advent of Code 2025 - Day 2
# https://adventofcode.com/2025/day/2
# Author: Alexandre MALFREYT

from typing import Literal

from sympy import Li

# Parse input
with open('input.txt', 'r') as f:
    ranges = [tuple(map(int, line.split('-'))) for line in f.read().strip().split(',')]

# Functions
def find_invalid_ids(ranges, method: Literal["repeated_twice", "repeated_any"]):
    total = 0
    for r_start, r_end in ranges:
        for n in range(r_start, r_end + 1):
            n_str = str(n)
            
            # Part 1
            if method == "repeated_twice":
                if not len(n_str)%2 and n_str[:len(n_str)//2] == n_str[len(n_str)//2:]:
                    total += n

            # Part 2
            if method == "repeated_any":
                for size in range(1, len(n_str)//2 + 1):
                    if len(n_str) % size: continue
                    if all(n_str[i:i+size] == n_str[:size] for i in range(0, len(n_str), size)):
                        total += n
                        break # prevent double counting (e.g. 2222 for size 1 and 2)
    
    return total


# Part 1 & 2
def part1(ranges):
    return find_invalid_ids(ranges, method="repeated_twice")

def part2(ranges):
    return find_invalid_ids(ranges, method="repeated_any")

# Tests
ranges_example = [(11,22), (95,115), (998,1012), (1188511880,1188511890), (222220,222224), (1698522,1698528), (446443,446449), (38593856,38593862), (565653,565659), (824824821,824824827), (2121212118,2121212124)]

assert part1(ranges_example) == 1227775554
assert part2(ranges_example) == 4174379265


# Results
print(f'Part 1 : {part1(ranges)}')
print(f'Part 2 : {part2(ranges)}')
