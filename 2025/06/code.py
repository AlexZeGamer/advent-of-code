# Advent of Code 2025 - Day 6
# https://adventofcode.com/2025/day/6
# Author: Alexandre MALFREYT

# Comment (part 1): Today I forgot my laptop so I'm forced to do it on my phone...
#                   Fortunately today's challenge seems easy? at least part 1

# Comment (part 2): Completely different parsing, but same logic.
#                   Wasn't too complicated, just a bit tricky to write on a smartphone

# Parse input
with open('input.txt', 'r') as f:
    lines = [l.strip("\n") for l in f.readlines()]

def parse_part1(lines):
    op_numbers = [[int(x) for x in y.strip().split()] for y in lines[:-1]]
    op_numbers = list(map(list, zip(*op_numbers))) # transpose op_numbers
    operators = lines[-1].strip().split()
    return op_numbers, operators

def parse_part2(lines):
    # parse from right to left to construct op_numbers_str
    nb_ops = len(lines[0])
    nb_numbers_per_op = len(lines)-1
    op_numbers_str = []
    
    def _check_separator(lines, i):
        return all([line[i]==" " for line in lines])

    op_numbers_str.append([])
    for i in range(nb_ops-1, -1, -1):
        if _check_separator(lines, i):
            op_numbers_str.append([])
        else:
            op_numbers_str[-1].append("")
            for j in range(nb_numbers_per_op):
                op_numbers_str[-1][-1] += lines[j][i]
    op_numbers = [[int(n.strip()) for n in op] for op in op_numbers_str]
    op_numbers = op_numbers[::-1] # reverse list for operations to be left to right
    operators = lines[-1].strip().split()
    return op_numbers, operators


# Functions
def calc_operations(op_numbers, operators):
    total = 0
    for i in range(len(operators)):
        subtotal = 0 if operators[i] == "+" else 1
        for number in op_numbers[i]:
            if operators[i] == "+":
                subtotal += number
            else: # "*"
                subtotal *= number
        total += subtotal
    return total


# Part 1 & 2
def part1(op_numbers, operators):
    return calc_operations(op_numbers, operators)

def part2(op_numbers, operators):
    return calc_operations(op_numbers, operators)


# Tests
example_lines = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".split("\n")[:-1]

assert part1(*parse_part1(example_lines)) == 4277556
assert part2(*parse_part2(example_lines)) == 3263827


# Results
print(f'Part 1 : {part1(*parse_part1(lines))}')
print(f'Part 2 : {part2(*parse_part2(lines))}')
