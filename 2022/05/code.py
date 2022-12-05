# Advent of Code 2022 - Day 5
# https://adventofcode.com/2022/day/5
# Author: Alexandre MALFREYT

import re

with open('input.txt', 'r') as f:
    lines = f.readlines()


# Part 1
message = ''

def read_stacks(lines: list) -> list:
    nbStacks = int(re.findall('(\d)', lines[-1])[-1]) 
    stacks = [[] for i in range(nbStacks)]
    for line in lines[:-1][::-1]:
        for i in range(nbStacks):
            elem = line[(i*4)+1]
            if elem != ' ':
                stacks[i].append(elem)
    return stacks

def read_message(stacks: list, moves: list) -> str:
    return ''.join([stack[-1] for stack in stacks])

def make_moves(stacks: list) -> list:
    # TODO
    return stacks


print(lines[lines.index('\n')+1:])
stacks = read_stacks(lines[:lines.index('\n')])
stacks = make_moves(stacks, lines[lines.index('\n')+1:])
message = read_message(stacks)

print(f'Part 1 : {message}')


# Part 2

