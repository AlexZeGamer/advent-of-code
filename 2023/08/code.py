# Advent of Code 2023 - Day 8
# https://adventofcode.com/2023/day/8
# Author: Alexandre MALFREYT

import re
import math

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

rl_instructions = lines[0]
paths = {}

for line in lines[2:]:
    # format : ABC = (DEF, HIJ)
    regex = re.search(r'(\w+) = \((\w+), (\w+)\)', line)
    paths[regex.group(1)] = (regex.group(2), regex.group(3)) if regex else None

# Part 1
example1 = ['RL', {'AAA': ('BBB', 'CCC'), 'BBB': ('DDD', 'EEE'), 'CCC': ('ZZZ', 'GGG'), 'DDD': ('DDD', 'DDD'), 'EEE': ('EEE', 'EEE'), 'GGG': ('GGG', 'GGG'), 'ZZZ': ('ZZZ', 'ZZZ')}]
example2 = ['LLR', {'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')}]

def get_path_length(rl_instructions, paths):
    path_length = 0
    current_location = 'AAA'
    current_instruction = 0
    while current_location != 'ZZZ':
        path_length += 1
        way = 0 if rl_instructions[current_instruction] == 'L' else 1
        current_location = paths[current_location][way]
        current_instruction = (current_instruction + 1) % len(rl_instructions)
    return path_length

assert get_path_length(*example1) == 2
assert get_path_length(*example2) == 6
result1 = get_path_length(rl_instructions, paths)

print(f'Part 1 : {result1}')


# Part 2
example3 = ['LR', {'11A': ('11B', 'XXX'), '11B': ('XXX', '11Z'), '11Z': ('11B', 'XXX'), '22A': ('22B', 'XXX'), '22B': ('22C', '22C'), '22C': ('22Z', '22Z'), '22Z': ('22B', '22B'), 'XXX': ('XXX', 'XXX')}]

import time
def calculate_time(previous_time = None):
    current_time = time.time()
    if previous_time:
        print(f'Elapsed time : {current_time - previous_time:.3f} s')
    return current_time, (current_time - previous_time) if previous_time else None

def next_step(rl_instructions, paths, current_location, current_instruction):
    way = 0 if rl_instructions[current_instruction] == 'L' else 1
    return paths[current_location][way]

def find_loop_lenght(rl_instructions, paths, start_location):
    current_location = start_location
    current_instruction = 0
    i = 0
    while current_location[-1] != 'Z':
        current_location = next_step(rl_instructions, paths, current_location, current_instruction)
        current_instruction = (current_instruction + 1) % len(rl_instructions)
        i += 1
    return i

def find_all_loop_lenghts(rl_instructions, paths, start_locations):
    return [find_loop_lenght(rl_instructions, paths, l) for l in start_locations]

def get_simultaneous_paths_length(rl_instructions, paths):
    current_locations = [l for l in paths.keys() if l[-1] == 'A']
    return math.lcm(*find_all_loop_lenghts(rl_instructions, paths, current_locations))

assert get_simultaneous_paths_length(*example3) == 6
result2 = get_simultaneous_paths_length(rl_instructions, paths)

print(f'Part 2 : {result2}')
