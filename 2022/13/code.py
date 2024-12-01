# Advent of Code 2022 - Day 13
# https://adventofcode.com/2022/day/13
# Author: Alexandre MALFREYT

from typing import List

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

allLists = []
for i in range(0, len(lines), 3):
    allLists.append([
        eval(lines[i]),
        eval(lines[i+1]),
    ])

# import pprint; pprint.pprint(allLists[:3])

# Example
# allLists = [
#     [
#         [1,1,3,1,1],
#         [1,1,5,1,1]
#     ],

#     [
#         [[1],[2,3,4]],
#         [[1],4]
#     ],

#     [
#         [9],
#         [[8,7,6]]
#     ],

#     [
#         [[4,4],4,4],
#         [[4,4],4,4,4]
#     ],

#     [
#         [7,7,7,7],
#         [7,7,7]
#     ],

#     [
#         [],
#         [3]
#     ],

#     [
#         [[[]]],
#         [[]]
#     ],

#     [
#         [1,[2,[3,[4,[5,6,7]]]],8,9],
#         [1,[2,[3,[4,[5,6,0]]]],8,9]
#     ],
# ]

# Part 1
total = 0

def compare(a: List, b: List):
    print(a, b)

    i = -1
    while i <= len(a) and i <= len(b):
        print(i)
        i += 1
        if i == len(a):
            return True
        if i == len(b):
            return False

        if a[i] == b[i]:
            continue
        if type(a[i]) == type(b[i]) == int:
            if a[i] < b[i]:
                return True
        if type(a[i]) == type(b[i]) == list:
            if compare(a[i], b[i]):
                return True
        if type(a[i]) == list and type(b[i]) == int:
            if compare(a[i], [b[i]]):
                return True
        if type(a[i]) == int and type(b[i]) == list:
            if compare([a[i]], b[i]):
                return True

        return False
    return True

i = 1
for lists in allLists:
    if compare(lists[0], lists[1]):
        print(f'Case {i} : True')
        total += i
    else:
        print(f'Case {i} : False')
    i += 1

print(f'Part 1 : {total}')


# Part 2
total = 0



print(f'Part 2 : {total}')
