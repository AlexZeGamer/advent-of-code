# Advent of Code 2022 - Day 7
# https://adventofcode.com/2022/day/7
# Author: Alexandre MALFREYT
from typing import List, Union

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')[:-1]


def read_input(lines: List[str]) -> dict:
    """ Read the input and return a tree representing the directory structure """
    root = {}
    pos = [] # We use a stack to keep track of the current position
    for line in lines:
        ### ignore the "ls" and "cd /" commands
        if line == "$ ls" or line == "$ cd /":
            continue
            
        ### "cd" commands are used to change the current position in the tree
        # We pop the stack if we go back to the parent directory
        elif line == "$ cd ..":
            pos.pop()
        # We push the stack if we go to a child directory
        elif line.startswith("$ cd "):
            pos.append(line[5:])

        ### Parsing "ls" output
        # If the line starts with "dir ", it's a directory
        elif line.startswith("dir "):
            # If we are at the root, we add the directory to the root
            if len(pos) == 0:
                root[line[4:]] = {}
            # Otherwise, we add the directory to the current position
            else:
                current = root
                for p in pos:
                    current = current[p]
                current[line[4:]] = {}
        
        # If the line doesn't start with "dir ", it's a file
        else:
            # If we are at the root, we add the file to the root
            if len(pos) == 0:
                root[line.split(' ')[1]] = int(line.split(' ')[0])
            # Otherwise, we add the file to the current position
            else:
                current = root
                for p in pos:
                    current = current[p]
                current[line.split(' ')[1]] = int(line.split(' ')[0])
    return root

def size(dirOrFile: Union[dict, int]) -> int:
    """ Recursively compute the size of a directory or a file """
    # If it's a file (represented by its size),
    # we return its size immediately
    if type(dirOrFile) == int:
        return dirOrFile
    
    # If it's a directory (represented by a dict of files/directories),
    # we compute the size of each element and sum them
    return sum([size(elem) for elem in dirOrFile.values()])


root = read_input(lines)

# Part 1
def solve_part1(dirOrFile: dict, n: int) -> int:
    # If it's a file (represented by its size),
    # we return 0 because it doesn't count in the total
    if type(dirOrFile) == int:
        return 0
    
    # If it's a directory (represented by a dict of files/directories),
    # we add the size of the directory to the total if it's smaller than n
    total = sum([solve_part1(elem, n) for elem in dirOrFile.values()])
    
    return total+size(dirOrFile) if size(dirOrFile) <= n else total

print(f'Part 1 : {solve_part1(root, 100_000)}')


# Part 2
diskSize = 70_000_000
usedSpace = size(root)
spaceNeeded = 30_000_000

def space_to_freed(root: dict, diskSize: int, spaceNeeded: int) -> int:
    """ Returns the number of bytes that need to be freed to add spaceNeeded bytes to a disk of size diskSize """
    return (usedSpace+spaceNeeded)-diskSize

def solve_part2(dirOrFile: dict, min: int, spaceToFreed: int) -> int:
    """ Returns the size of the smallest directory of the tree that can be deleted to free spaceToFreed bytes """
    for elem in dirOrFile.values():
        if type(dirOrFile) == int:
            return 0

        if type(elem) == dict:
            if spaceToFreed <= size(elem) <= min:
                min = size(elem)
            min = solve_part2(elem, min, spaceToFreed)
    
    return min
    

print(f'Part 2 : {solve_part2(root, diskSize, space_to_freed(root, diskSize, spaceNeeded))}')
