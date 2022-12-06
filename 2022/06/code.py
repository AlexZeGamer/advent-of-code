# Advent of Code 2022 - Day 6
# https://adventofcode.com/2022/day/6
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    text = f.read().replace('\n','')


# Part 1
SEQUENCE_SIZE = 4
for i in range(SEQUENCE_SIZE, len(text)):
    sequence = text[i-SEQUENCE_SIZE: i]
    print(sequence)

    found = False
    for j in range(4):
        for k in range(j+1,4):
            print(j, k)
            print(sequence[j], sequence[k])
            if sequence[j] == sequence[k]:
                found = True
    
    if not found:
        break

print(f'Part 1 : {i}')


# Part 2
total = 0



print(f'Part 2 : {total}')
