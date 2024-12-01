# Advent of Code 2024 - Day 1
# https://adventofcode.com/2024/day/1
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


# Part 1
total = 0

left_list = []
right_list = []
for line in lines:
    left, right = line.split('   ')
    left_list.append(int(left))
    right_list.append(int(right))

left_list.sort()
right_list.sort()

for left, right in zip(left_list, right_list):
    diff = abs(left - right)
    total += diff

print(f'Part 1 : {total}')


# Part 2
total = 0

for left in left_list:
    total += left * right_list.count(left)

print(f'Part 2 : {total}')
