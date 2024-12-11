# Advent of Code 2024 - Day 11
# https://adventofcode.com/2024/day/11
# Author: Alexandre MALFREYT

DEBUG = False

with open('input.txt', 'r') as f:
    stones = [int(x) for x in f.read().strip().split(' ')]

# Part 1
def simulate_blink_inplace(stones: list[int]) -> list[int]:
    i = 0
    print(f"Simulating blink on {stones}") if DEBUG else None
    while i < len(stones):
        print(f"i={i}, stones[i]={stones[i]}") if DEBUG else None
        stone = stones[i]
        stone_str = str(stone)
        nb_digits = len(stone_str)
        
        if stone == 0:
            print("  stone is 0") if DEBUG else None
            stones[i] = 1

        elif nb_digits % 2 == 0:
            print("  nb_digits is even") if DEBUG else None
            stones[i] = int(stone_str[:nb_digits//2])
            stones.insert(i+1, int(stone_str[nb_digits//2:]))
            print(f"  Inserted {stones[i+1]} at position {i+1}") if DEBUG else None
            i += 1 # Skip the next stone since we just inserted a new one
        
        else:
            print("  nb_digits is odd") if DEBUG else None
            stones[i] = stone * 2024

        i += 1

def simulate_n_blinks_inplace(stones: list[int], nb_blinks: int, print_steps: bool = False) -> None:
    print("Initial arrangement:") if print_steps else None
    print(" ".join(str(x) for x in stones)) if print_steps else None
    print() if print_steps else None
    for i in range(nb_blinks):
        print(f"Simulating blink {i+1}")
        simulate_blink_inplace(stones)
        print(f"After {i+1} blink{'s' if i > 0 else ''}:") if print_steps else None
        print(" ".join(str(x) for x in stones)) if print_steps else None
        print() if print_steps else None

simulate_n_blinks_inplace(stones, 25)

print(f'Part 1 : {len(stones)}')


# Part 2
total = 0

simulate_n_blinks_inplace(stones, 75-25) # 75 blinks - 25 already done

print(f'Part 2 : {len(stones)}')

# Examples
print("--- Examples ---")

stones_example1 = [0, 1, 10, 99, 999]  # Example 1
stones_example2 = [125, 17]  # Example 2

print("Example 1:")
simulate_n_blinks_inplace(stones_example1, 1, print_steps=True)
assert stones_example1 == [1, 2024, 1, 0, 9, 9, 2021976]

print("Example 2:")
simulate_n_blinks_inplace(stones_example2, 6, print_steps=True)
assert stones_example2 == [2097446912, 14168, 4048, 2, 0, 2, 4, 40, 48, 2024, 40, 48, 80, 96, 2, 8, 6, 7, 6, 0, 3, 2]
