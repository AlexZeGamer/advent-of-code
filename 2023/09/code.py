# Advent of Code 2023 - Day 9
# https://adventofcode.com/2023/day/9
# Author: Alexandre MALFREYT

from typing import List

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

lines = [[int(d) for d in line.split(' ')] for line in lines]

# Example:
# lines = [
#     [0, 3, 6, 9, 12, 15],
#     [1, 3, 6, 10, 15, 21],
#     [10, 13, 16, 21, 30, 45],
# ]

# Part 1
def all_null(line: List[int]) -> bool:
    return all([d == 0 for d in line])

def compute_differences(line: List[int]):
    if all_null(line):
        return []

    differences = [line[i+1] - line[i] for i in range(len(line)-1)]
    return [differences] + compute_differences(differences)
    
def predict(line: List[int], diff: List[int]) -> int:
    diff[-1] += [0]
    for i in range(len(diff)-2, -1, -1):
        diff[i] += [diff[i][-1] + diff[i+1][-1]]
    
    return line[-1] + diff[0][-1]

total = 0
for line in lines:
    differences = compute_differences(line)
    total += predict(line, differences)

print(f'Part 1 : {total}')


# Part 2
def predict_history(line: List[int], diff: List[int]) -> int:
    diff[-1] = [0] + diff[-1]
    for i in range(len(diff)-2, -1, -1):
        diff[i] = [diff[i][0] - diff[i+1][0]] + diff[i]

    return line[0] - diff[0][0]

total = 0
for i, line in enumerate(lines):
    differences = compute_differences(line)
    res = predict_history(line, differences)
    total += res

print(f'Part 2 : {total}')
