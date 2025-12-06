# Advent of Code 2025 - Day 6
# https://adventofcode.com/2025/day/6
# Author: Alexandre MALFREYT

# Comment (part 1): Today I forgot my laptop so I'm forced to do it on my phone...
#                   Fortunately today's challenge seems easy? at least part 1

# Parse input
with open('input.txt', 'r') as f:
    lines = f.readlines()
    numbers = [[int(x) for x in y.strip().split()] for y in lines[:-1]]
    numbers = list(map(list, zip(*numbers))) # transpose numbers
    operators = lines[-1].strip().split()


# Functions
...


# Part 1 & 2
def part1(numbers, operators):
    total = 0
    for i in range(len(operators)):
        subtotal = 0 if operators[i] == "+" else 1
        for number in numbers[i]:
            if operators[i] == "+":
                subtotal += number
            else: # "*"
                subtotal *= number
        total += subtotal
    return total

def part2(numbers, operators):
    return ...


# Tests
numbers_example = [[123, 45, 6], [328, 64, 98], [51, 387, 215], [64, 23, 314]]
operators_example = ["*", "+", "*", "+"]

assert part1(numbers_example, operators_example) == 4277556
assert part2(numbers_example, operators_example) == ...


# Results
print(f'Part 1 : {part1(numbers, operators)}')
print(f'Part 2 : {part2(numbers, operators)}')
