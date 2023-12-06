# Advent of Code 2023 - Day 6
# https://adventofcode.com/2023/day/6
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

times = [int(val) for val in lines[0].split()[1:]]
distances = [int(val) for val in lines[1].split()[1:]]

# Example:
# Time:      7  15   30
# Distance:  9  40  200
# times =     [7, 15,  30]
# distances = [9, 40, 200]

# Part 1
total = 1

if len(times) != len(distances):
    raise Exception('Times and distances have different lengths')

for i in range(len(times)):
    number_of_ways_to_win = 0
    for time_pressing_button in range(times[i]):
        time = times[i]
        speed = time_pressing_button
        remaining_time = time - time_pressing_button
        distance_travelled = remaining_time * speed
        record = distances[i]
        if distance_travelled > record:
            number_of_ways_to_win += 1
    total *= number_of_ways_to_win

print(f'Part 1 : {total}')


# Part 2
total = 0



print(f'Part 2 : {total}')
