# Advent of Code 2022 - Day 9
# https://adventofcode.com/2022/day/9
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
print(lines)

##############
#      y     #
#      ↑     #
# -x <- -> x #
#      ↓     #
#     -y     #
##############


# Part 1
visited = [] # [] of (x, y) of visited points by the tail
tail = {'x': 0, 'y': 0}
head = {'x': 0, 'y': 0}

def move_tail(head: dict, tail: dict) -> dict:
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

    

for line in lines:
    direction = line[0]
    distance = int(line[1:])
    for i in range(distance):
        if direction == 'U':
            head['y'] += 1
        elif direction == 'D':
            head['y'] -= 1
        elif direction == 'R':
            head['x'] += 1
        elif direction == 'L':
            head['x'] -= 1

        move_tail(head, tail)
        if (tail['x'], tail['y']) not in visited:
            visited.append((tail['x'], tail['y']))
        print(f'{direction}{distance} : {head} - {tail}')

print(f'Part 1 : {len(visited)}')

# Part 2
total = 0

print(f'Part 2 : {total}')
