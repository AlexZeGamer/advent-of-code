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

DEBUG = False

def calculate(equation, operators):
    """
    Returns if the equation can be calculated with the given operators to get the expected result or not

    Args:
        equation (tuple[int, list[int]]): The equation to calculate
        operators (list): The list of operators to use to calculate the equation (possible values: '+', '*', '||')

    Returns:
        bool: True if the equation can be calculated with the given operators to get the expected result, False otherwise

    Examples:
        - calculate((190, [10, 19]), ['+', '*']) -> True
        - calculate((83, [17, 5]), ['+', '*']) -> False
    """
    print(f'\nEquation: {equation}') if DEBUG else None

    expected_result = equation[0]
    operands = equation[1]

    # We try all possible combinations of + and * operators
    for comb in itertools.product(operators, repeat=len(operands)-1):
        print(comb) if DEBUG else None
        sub_total = operands[0]

        # We calculate the result of the equation with the current combination of operators
        for i, operator in enumerate(comb):
            if operator == '+':
                sub_total += operands[i+1]
            elif operator == '*':
                sub_total *= operands[i+1]
            elif operator == '||':
                # TODO
                ...

        # If the result is the same as the expected result, we add it to the total
        equation_str = ' '.join([str(n) + ' ' + comb[i] for i, n in enumerate(operands[:-1])]) + ' ' + str(operands[-1])
        if sub_total == expected_result:
            if DEBUG:
                print('\033[92m', end='')
                print(f'{equation_str} = {expected_result}')
                print('\033[0m', end='')
            return True
        else:
            if DEBUG:
                print('\033[91m', end='')
                print(f'{equation_str} = {sub_total} != {expected_result}')
                print('\033[0m', end='')
    
    return False

# Part 1
operators = ["+", "*"]


total = 0
for equation in equations:
    expected_result = equation[0]
    if calculate(equation, operators):
        total += expected_result

print(f'Part 1 : {total}')

# Part 2
operators = ['+', '*', '||']

total = 0
# for equation in equations:
#     expected_result = equation[0]
#     if calculate(equation, operators):
#         total += expected_result

print(f'Part 2 : {total}')