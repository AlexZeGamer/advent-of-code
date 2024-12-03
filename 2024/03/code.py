# Advent of Code 2024 - Day 3
# https://adventofcode.com/2024/day/3
# Author: Alexandre MALFREYT

import re

with open('input.txt', 'r') as f:
    text = f.read()

# text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Part 1
total = 0

mul_regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
for match in mul_regex.finditer(text):
    a, b = map(int, match.groups())
    total += a * b

print(f'Part 1 : {total}')


# Part 2
total = 0

# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

do_regex = re.compile(r'do\(\)')
dont_regex = re.compile(r"don't\(\)")

do_matches = [match.start() for match in do_regex.finditer(text)] # [(pos1), (pos2), ...]
dont_matches = [match.start() for match in dont_regex.finditer(text)] # [(pos1), (pos2), ...]
mul_matches = [(match.start(), *map(int, match.groups())) for match in mul_regex.finditer(text)] # [(pos1, a1, b1), (pos2, a2, b2), ...]

last_pos = -1
for mul_match in mul_matches:
    pos = mul_match[0]
    a, b = mul_match[1:]
    
    skip = False

    # filter all dont matches between the last mul that was not skipped and current match
    last_dont_pos = -1
    for dont_pos in dont_matches:
        if last_pos < dont_pos < pos:
            last_dont_pos = dont_pos
            skip = True
            break
    
    # filter all do matches between the last dont in the range and current match
    for do_pos in do_matches:
        if last_dont_pos < do_pos < pos:
            skip = False
            break
    
    if not skip:
        last_pos = pos
        total += a * b

print(f'Part 2 : {total}')
