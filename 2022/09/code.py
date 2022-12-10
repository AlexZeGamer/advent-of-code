# Advent of Code 2022 - Day 9
# https://adventofcode.com/2022/day/9
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Example 1
# lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """.splitlines()

# Example 2
# lines = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20
# """.splitlines()

##############
#      y     #
#      ↑     #
# -x <- -> x #
#      ↓     #
#     -y     #
##############


def move_head(head: dict, direction: str) -> dict:
    """ Move the head one time in the given direction and return the new position """

    if direction == 'U':
        head['y'] += 1
    elif direction == 'D':
        head['y'] -= 1
    elif direction == 'R':
        head['x'] += 1
    elif direction == 'L':
        head['x'] -= 1
        
    return head

def move_tail(head: dict, tail: dict) -> dict:
    """ Move the tail one time to follow the head and return the new position """

    # If head and tail are at the same position, we don't move the tail
    if head == tail:
        return tail
    
    # If tail touches the head (directly or diagonaly), we don't move the tail
    if abs(head['x'] - tail['x']) <= 1 and abs(head['y'] - tail['y']) <= 1:
        return tail
    
    # If head and tail are on the same axis, we move the tail on the same axis
    if tail['x'] == head['x']:
        if tail['y'] > head['y']:
            tail['y'] -= 1
        else:
            tail['y'] += 1
        return tail
    elif tail['y'] == head['y']:
        if tail['x'] > head['x']:
            tail['x'] -= 1
        else:
            tail['x'] += 1
        return tail
    
    # If head and tail are on different axis, we move the tail diagonaly
    if tail['x'] > head['x'] and tail['y'] > head['y']:
        tail['x'] -= 1
        tail['y'] -= 1
    elif tail['x'] > head['x'] and tail['y'] < head['y']:
        tail['x'] -= 1
        tail['y'] += 1
    elif tail['x'] < head['x'] and tail['y'] > head['y']:
        tail['x'] += 1
        tail['y'] -= 1
    elif tail['x'] < head['x'] and tail['y'] < head['y']:
        tail['x'] += 1
        tail['y'] += 1
    return tail


# Part 1
visited = [] # [] of (x, y) of visited points by the tail
tail = {'x': 0, 'y': 0}
head = {'x': 0, 'y': 0}

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    for i in range(distance):
        head = move_head(head, direction)
        tail = move_tail(head, tail)
        if (tail['x'], tail['y']) not in visited:
            visited.append((tail['x'], tail['y']))

print(f'Part 1 : {len(visited)}')


# Part 2
visited = [] # [] of (x, y) of visited points by the tail

# 0 is the head, 1-9 is the tail
rope = [{'x': 0, 'y': 0} for _ in range(10)]

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    for i in range(distance):
        rope[0] = move_head(rope[0], direction)

        # Each tail is the head of the next tail
        for i in range(1, len(rope)):
            rope[i] = move_tail(rope[i-1], rope[i])

        # Add the new position of the tail to the list of visited points
        if (rope[i]['x'], rope[i]['y']) not in visited:
            visited.append((rope[i]['x'], rope[i]['y']))

print(f'Part 2 : {len(visited)}')
