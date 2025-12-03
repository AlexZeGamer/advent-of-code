# Advent of Code 2025 - Day 3
# https://adventofcode.com/2025/day/3
# Author: Alexandre MALFREYT

# Parse input
with open('input.txt', 'r') as f:
    battery_banks = [[int(x) for x in y.strip()] for y in f.readlines()]


# Functions
# https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
_max_idx = lambda lst: max(range(len(lst)), key=lst.__getitem__)

def find_highest_joltage(battery_bank: list[int], nb_batteries: int) -> int:
    match nb_batteries:
        case _ if nb_batteries < 0:
            raise ValueError('Number of batteries cannot be negative')
        case 0:
            return 0
        case 1:
            return max(battery_bank)
        case 2: # technically the same logic as for 3 or more batteries, but more readable and was done for part 1 first
            # first digit: find the battery with the highest joltage (except the last one)
            first_digit_idx = _max_idx(battery_bank[:-1])
            first_digit = battery_bank[first_digit_idx]
            # second digit: get the highest joltage of the batteries after the highest one
            second_digit = max(battery_bank[first_digit_idx + 1:])
            return first_digit*10 + second_digit
        case _ if nb_batteries >= 3: # 3 or more batteries (as many digits as the number of batteries)
            total = 0
            remaining_batteries = nb_batteries # could have been done recursively too by passing nb_batteries - 1 each time
            current_index = -1 # no battery selected yet, place cursor before the first one
            while remaining_batteries > 0:
                # for each digit, find the highest battery among the remaining ones between:
                # - the last one selected (current_index, the last digit added to the result, you can't take numbers before that since the order matters)
                # - and the last possible one (at -(remaining_batteries - 1), because we need to leave enough batteries for the remaining digits)
                next_index = _max_idx(battery_bank[current_index + 1:-(remaining_batteries - 1) or None]) + current_index + 1
                total += battery_bank[next_index] * (10 ** (remaining_batteries - 1)) # add the digit at the correct place value
                current_index = next_index
                remaining_batteries -= 1
            return total


# Part 1 & 2
def part1(battery_banks: list[list[int]]) -> int:
    total = 0
    for battery_bank in battery_banks:
        total += find_highest_joltage(battery_bank, 2)
    return total

def part2(battery_banks: list[list[int]]) -> int:
    total = 0
    for battery_bank in battery_banks:
        total += find_highest_joltage(battery_bank, 12)
    return total


# Tests
example = [
    [9,8,7,6,5,4,3,2,1,1,1,1,1,1,1],
    [8,1,1,1,1,1,1,1,1,1,1,1,1,1,9],
    [2,3,4,2,3,4,2,3,4,2,3,4,2,7,8],
    [8,1,8,1,8,1,9,1,1,1,1,2,1,1,1],
]

assert part1(example) == 357
assert part2(example) == 3121910778619


# Results
print(f'Part 1 : {part1(battery_banks)}')
print(f'Part 2 : {part2(battery_banks)}')
