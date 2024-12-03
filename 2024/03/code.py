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

text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

do_regex = re.compile(r'do\(\)')
dont_regex = re.compile(r"don't\(\)")

do_matches = [match.start() for match in do_regex.finditer(text)] # [(pos1), (pos2), ...]
dont_matches = [match.start() for match in dont_regex.finditer(text)] # [(pos1), (pos2), ...]
mul_matches = [(match.start(), *map(int, match.groups())) for match in mul_regex.finditer(text)] # [(pos1, a1, b1), (pos2, a2, b2), ...]

for mul_match in mul_matches:
    if any(do_match < mul_match[0] < dont_match for do_match in do_matches for dont_match in dont_matches):
        continue
    a, b = mul_match[1:]
    total += a * b

print(f'Part 2 : {total}')
