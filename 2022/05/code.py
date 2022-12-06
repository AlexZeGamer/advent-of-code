# Advent of Code 2022 - Day 5
# https://adventofcode.com/2022/day/5
# Author: Alexandre MALFREYT

import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

def parse_stacks(lines: list) -> list:
    """ Parse stacks from the input file """

    # number of stacks (last number of the line with the stacks numbers)
    nbStacks = int(re.findall('(\d+)', lines[-1])[-1])

    # create empty stacks
    stacks = [[] for _ in range(nbStacks)]

    # "[X] [Y] [Z]" -> ["X", "Y", "Z"]
    for line in lines[:-1][::-1]:
        for i in range(nbStacks):
            elem = line[(i*4)+1]
            if elem != ' ':
                stacks[i].append(elem)

    return stacks

def read_message(stacks: list) -> str:
    """ Get the final message """
    # get le last letter (=top) of each stack
    return ''.join([stack[-1] for stack in stacks])


# Part 1
def CrateMover9000(stacks: list, moves: list) -> list:
    """ Apply the moves (of the form "move X from Y to Z") to the stacks
        (One crate at a time : CrateMover 9000)"""
    for move in moves:
        # parse numbers from a string of the form "move X from Y to Z"
        nbMoves, start, end = [int(x) for x in re.findall('\d+', move)]

        # LIFO
        for _ in range(nbMoves):
            crate = stacks[start-1].pop()
            stacks[end-1].append(crate)

    return stacks

stacks = parse_stacks(lines[:lines.index('\n')])
stacks = CrateMover9000(stacks, lines[lines.index('\n')+1:])
message = read_message(stacks)

print(f'Part 1 : {message}')


# Part 2
def CrateMover9001(stacks: list, moves: list) -> list:
    """ Apply the moves (of the form "move X from Y to Z") to the stacks
        (Multiple crate at once : CrateMover 9001)"""
    for move in moves:
        # parse numbers from a string of the form "move X from Y to Z"
        nbMoves, start, end = [int(x) for x in re.findall('\d+', move)]

        # FIFO
        queue = []
        for _ in range(nbMoves):
            queue.append(
                stacks[start-1].pop()
            )
        
        for crate in queue[::-1]:
            stacks[end-1].append(crate)

    return stacks


stacks = parse_stacks(lines[:lines.index('\n')])
stacks = CrateMover9001(stacks, lines[lines.index('\n')+1:])
message = read_message(stacks)

print(f'Part 2 : {message}')
