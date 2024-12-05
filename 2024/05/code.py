# Advent of Code 2024 - Day 5
# https://adventofcode.com/2024/day/5
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# get the empty line and split the list into two parts
empty_line = lines.index('')

rules = lines[:empty_line]
updates = lines[empty_line + 1:]

rules = [tuple(map(int, line.split('|'))) for line in rules]
updates = [list(map(int, line.split(','))) for line in updates]

# Example
# rules = [
#     (47, 53),
#     (97, 13),
#     (97, 61),
#     (97, 47),
#     (75, 29),
#     (61, 13),
#     (75, 53),
#     (29, 13),
#     (97, 29),
#     (53, 29),
#     (61, 53),
#     (97, 53),
#     (61, 29),
#     (47, 13),
#     (75, 47),
#     (97, 75),
#     (47, 61),
#     (75, 61),
#     (47, 29),
#     (75, 13),
#     (53, 13),
# ]

# updates = [
#     [75, 47, 61, 53, 29],
#     [97, 61, 53, 29, 13],
#     [75, 29, 13],
#     [75, 97, 47, 61, 53],
#     [61, 13, 29],
#     [97, 13, 75, 29, 47],
# ]

# Part 1
valid_updates = []
for update in updates:
    valid = True

    for rule in rules:
        if not all(x in update for x in rule):
            continue

        # if not (all(update.index(rule[i]) < update.index(rule[i + 1]) for i in range(len(rule) - 1))):
        if not (update.index(rule[0]) < update.index(rule[1])):
            valid = False
            break
    
    if valid:
        valid_updates.append(update)

total = 0
for update in valid_updates:
    total += update[len(update)//2]

print(f'Part 1 : {total}')


# Part 2
total = 0


print(f'Part 2 : {total}')
