# Advent of Code 2024 - Day 7
# https://adventofcode.com/2024/day/7
# Author: Alexandre MALFREYT

import itertools

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

equations = [
    (                                                   # (
        int(l.split(': ')[0]),                          # 123,
        [int(n) for n in l.split(': ')[1].split(' ')]   # [4, 5, 6]
    ) for l in lines                                    # )
]

# Example input
# equations = [
#     ( 190,    [10, 19]        ),
#     ( 3267,   [81, 40, 27]    ),
#     ( 83,     [17, 5]         ),
#     ( 156,    [15, 6]         ),
#     ( 7290,   [6, 8, 6, 15]   ),
#     ( 161011, [16, 10, 13]    ),
#     ( 192,    [17, 8, 14]     ),
#     ( 21037,  [9, 7, 18, 13]  ),
#     ( 292,    [11, 6, 16, 20] ),
# ]

# Part 1
DEBUG_PART1 = False

operatiors = ['+', '*']

total = 0
for equation in equations:
    print(f'Equation: {equation}') if DEBUG_PART1 else None
    # We try all possible combinations of + and * operators
    for comb in itertools.product(operatiors, repeat=len(equation[1])-1):
        print(comb) if DEBUG_PART1 else None
        sub_total = equation[1][0]

        # We calculate the result of the equation
        for i, operator in enumerate(comb):
            if operator == '+':
                sub_total += equation[1][i+1]
            elif operator == '*':
                sub_total *= equation[1][i+1]

        # If the result is the same as the expected result, we add it to the total
        equation_str = ' '.join([str(n) + ' ' + comb[i] for i, n in enumerate(equation[1][:-1])]) + ' ' + str(equation[1][-1])
        if sub_total == equation[0]:
            total += equation[0]
            if DEBUG_PART1:
                print('\033[92m', end='')
                print(f'{equation_str} = {equation[0]}')
                print('\033[0m', end='')
            break
        else:
            if DEBUG_PART1:
                print('\033[91m', end='')
                print(f'{equation_str} = {sub_total} != {equation[0]}')
                print('\033[0m', end='')
    print() if DEBUG_PART1 else None

print(f'Part 1 : {total}')


# Part 2
total = 0


print(f'Part 2 : {total}')
