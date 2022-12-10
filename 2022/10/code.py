# Advent of Code 2022 - Day 10
# https://adventofcode.com/2022/day/10
# Author: Alexandre MALFREYT
from typing import List

# with open('example.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def signal_strength(i: int, X: int) -> int:
    if not (i-20)%40:
        return i * X
    return 0


# Part 1
total = 0
X = 1
tick = 0

for i in range(len(lines)):
    instruction = lines[i]

    if instruction == 'noop':
        tick += 1
        total += signal_strength(tick, X)

    elif instruction.startswith('addx'):
        value = int(instruction.split(' ')[1])

        for i in range(2):
            tick += 1
            total += signal_strength(tick, X)
        
        X += value


print(f'Part 1 : {total}')


# Part 2
DARK = '.'
LIGHT = '#'
HEIGHT = 6
WIDTH = 40

def show_screen(CRT: List[List[str]]) -> None:
    for i in range(len(CRT)):
        print(''.join(CRT[i]))

def draw_pixel(CRT: List[List[str]], tick: int) -> List[List[str]]:
    x = (tick-1) // WIDTH
    y = (tick-1) % WIDTH

    # Sprite position in a line
    # The sprite is 3 pixels wide
    sprite_pos = range(X-1, X+2)

    if y in sprite_pos:
        CRT[x][y] = LIGHT
    else:
        CRT[x][y] = DARK
    
    return CRT

CRT = [ [' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
        
X = 1
tick = 0

for i in range(len(lines)):
    instruction = lines[i]

    if instruction == 'noop':
        tick += 1
        CRT = draw_pixel(CRT, tick)

    elif instruction.startswith('addx'):
        value = int(instruction.split(' ')[1])

        for i in range(2):
            tick += 1
            CRT = draw_pixel(CRT, tick)

        X += value


print(f'Part 2 :')
show_screen(CRT)
