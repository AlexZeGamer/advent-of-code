# Advent of Code 2025 - Day 5
# https://adventofcode.com/2025/day/5
# Author: Alexandre MALFREYT

# Comment (Part 1): This one seems too easy... I'm afraid of part 2.
# Comment (Part 2): Ok that was a bit tricky but fun to solve (naive solution clearly wouldn't
#                   work here, ranges are so big it gets stuck on the very first range and runs
#                   out of memory)

# Parse input
with open('input.txt', 'r') as f:
    lines = f.readlines()
    separator = lines.index('\n')
    fresh_ranges = []
    for line in lines[:separator]:
        start, end = map(int, line.strip().split('-'))
        fresh_ranges.append(range(start, end + 1))
    ingredients = [int(line.strip()) for line in lines[separator+1:]]

    # print("Fresh ranges:")
    # for i in range(len(fresh_ranges)):
    #     print(f'  Range {i+1}: {fresh_ranges[i]}')

    # print("\nIngredients:")
    # for i in range(len(ingredients)):
    #     print(f'  Ingredient {i+1}: {ingredients[i]}')


# Part 1 & 2
def part1(fresh_ranges, ingredients):
    return len([ing for ing in ingredients if any(ing in r for r in fresh_ranges)])

def part2(fresh_ranges):
    nb_fresh_ids = 0
    for i, r in enumerate(fresh_ranges):
        # check if this range overlaps with any other already added range (min or max in any of previous ranges), and cut it if so
        for prev_r in fresh_ranges[:i]:
            if r.start in prev_r:
                r = range(prev_r.stop, r.stop + 1)
            if r.stop in prev_r:
                r = range(r.start, prev_r.start)
        if r.start < r.stop:
            nb_fresh_ids += len(r)
    return nb_fresh_ids
        

# Tests
fresh_ranges_example = [range(3, 5+1), range(10, 14+1), range(16, 20+1), range(12, 18+1)]
ingredients_example = [1,5,8,11,17,32]

assert part1(fresh_ranges_example, ingredients_example) == 3
assert part2(fresh_ranges_example) == 14


# Results
print(f'Part 1 : {part1(fresh_ranges, ingredients)}')
print(f'Part 2 : {part2(fresh_ranges)}')
