# Advent of Code 2024 - Day 3
# https://adventofcode.com/2024/day/3
# Author: Alexandre MALFREYT

import re

with open('input.txt', 'r') as f:
    text = f.read()

# text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

# Part 1
total = 0

regex = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
for match in regex.finditer(text):
    a, b = map(int, match.groups())
    total += a * b

print(f'Part 1 : {total}')


# Part 2
total = 0



print(f'Part 2 : {total}')
