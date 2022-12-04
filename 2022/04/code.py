# Advent of Code 2022 - Day 4
# https://adventofcode.com/2022/day/4
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    pairs = [line.replace('\n', '') for line in f.readlines()]
    
    # "a-b,xy" => [['a', 'b'], ['x', 'y']]
    pairs = [
        [
            [
                int(x)
                for x in elf.split('-')
            ]
            for elf in pair.split(',')
        ]
        for pair in pairs
    ]


# Part 1
total = 0
for pair in pairs:
    # Check if the range of one elf if fully included in the range of the other
    if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1])\
    or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
        total += 1

print(f'Part 1 : {total}')


# Part 2
total = 0
for pair in pairs:
    # Check if the range of one elf overlaps the range of the other
    if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0])\
    or (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]):
        total += 1

print(f'Part 2 : {total}')
