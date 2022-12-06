# Advent of Code 2022 - Day 6
# https://adventofcode.com/2022/day/6
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    text = f.read().replace('\n','')


def find_start_of_packet(data: str, sequenceSize: int) -> int:
    """ Returns the index of the start-of-packet marker """
    for i in range(sequenceSize, len(data)):
        sequence = data[i-sequenceSize: i]

        found = False
        for j in range(sequenceSize):
            for k in range(j+1,sequenceSize):
                if sequence[j] == sequence[k]:
                    found = True
        
        if not found:
            return i


# Part 1
print(f'Part 1 : {find_start_of_packet(text, 4)}')


# Part 2
print(f'Part 2 : {find_start_of_packet(text, 14)}')
