# Advent of Code 2025 - Day 5
# https://adventofcode.com/2025/day/5
# Author: Alexandre MALFREYT

# Comment (Part 1): This one seems too easy... I'm afraid of part 2.
# Comment (Part 2): Ok that was definitly trickier but fun to solve!
#                   My solution is a bit verbose but covers all cases.
#                   (naive solution clearly wouldn't work here, ranges are so big
#                   it gets stuck on the very first range and runs out of memory)

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

def part2(fresh_ranges, verbose=False):
    nb_fresh_ids = 0
    for i, _ in enumerate(fresh_ranges): # this is so the loop can expand the list while iterating
        print(f'Processing range {fresh_ranges[i].start}-{fresh_ranges[i].stop-1}...') if verbose else None
        # check if this range overlaps with any other already added range (min or max in any of previous ranges), and cut it if so
        for prev_r in fresh_ranges[:i]:
            overlap = True
            stop = False
            while overlap and not stop:
                overlap = False
                # start of current range overlaps with previous range
                if fresh_ranges[i].start in prev_r:
                    fresh_ranges[i] = range(prev_r.stop, fresh_ranges[i].stop)
                    print(f'  Start overlaps with previous range {prev_r.start}-{prev_r.stop-1}, cutting to {fresh_ranges[i].start}-{fresh_ranges[i].stop-1}') if verbose else None
                    overlap = True
                # end of current range overlaps with previous range
                if fresh_ranges[i].stop-1 in prev_r:
                    fresh_ranges[i] = range(fresh_ranges[i].start, prev_r.start)
                    print(f'  End overlaps with previous range {prev_r.start}-{prev_r.stop-1}, cutting to {fresh_ranges[i].start}-{fresh_ranges[i].stop-1}') if verbose else None
                    overlap = True
                # previous range fully overlaps with current range
                if fresh_ranges[i].start >= prev_r.start and fresh_ranges[i].stop <= prev_r.stop:
                    print(f'  Previous range fully overlaps with current range {prev_r.start}-{prev_r.stop-1} so no fresh IDs to add, skipping...') if verbose else None
                    stop = True
                # current range fully overlaps with previous range, need to split it into two parts
                if fresh_ranges[i].start < prev_r.start and fresh_ranges[i].stop > prev_r.stop:
                    print(f'  Current range {prev_r.start}-{prev_r.stop-1} fully overlaps with previous range, cutting to two parts...') if verbose else None
                    first_part = range(fresh_ranges[i].start, prev_r.start)
                    second_part = range(prev_r.stop, fresh_ranges[i].stop)
                    fresh_ranges += [first_part, second_part]
                    fresh_ranges[i] = range(0, 0)  # mark current range as empty
                    print(f'    First part: {first_part.start}-{first_part.stop-1}, Second part: {second_part.start}-{second_part.stop-1}') if verbose else None
                    stop = True
            if stop: break
        if fresh_ranges[i].start < fresh_ranges[i].stop:
            print(f'  Adding range {fresh_ranges[i].start}-{fresh_ranges[i].stop-1} with {len(fresh_ranges[i])} fresh IDs') if verbose else None
            fresh_ranges[i] = range(fresh_ranges[i].start, fresh_ranges[i].stop)
            nb_fresh_ids += len(fresh_ranges[i])
    return nb_fresh_ids


# Tests
fresh_ranges_example = [range(3, 5+1), range(10, 14+1), range(16, 20+1), range(12, 18+1)]
ingredients_example = [1,5,8,11,17,32]

assert part1(fresh_ranges_example, ingredients_example) == 3
assert part2(fresh_ranges_example) == 14


# Results
print(f'Part 1 : {part1(fresh_ranges, ingredients)}')
print(f'Part 2 : {part2(fresh_ranges)}')
