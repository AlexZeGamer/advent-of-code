# Advent of Code 2024 - Day 2
# https://adventofcode.com/2024/day/2
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

reports = [
    [int(level) for level in line.split(' ')]
    for line in lines
]

# reports = [
#     [7, 6, 4, 2, 1],
#     [1, 2, 7, 8, 9],
#     [9, 7, 6, 2, 1],
#     [1, 3, 2, 4, 5],
#     [8, 6, 4, 4, 1],
#     [1, 3, 6, 7, 9],
# ]

# Part 1
total = 0

def is_safe(report):
    # Conditions : increasing or decreasing by step between 1 and 3 included
    return all(report[i]+1 <= report[i+1] <= report[i]+3 for i in range(len(report)-1)) \
    or     all(report[i]-1 >= report[i+1] >= report[i]-3 for i in range(len(report)-1))

for report in reports:
    if is_safe(report):
        total += 1

print(f'Part 1 : {total}')


# Part 2
total = 0


print(f'Part 2 : {total}')
