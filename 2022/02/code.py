# https://adventofcode.com/2022/day/2

with open('input.txt', 'r') as f:
    text = f.read()

shapes = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'X' : 1,
    'Y' : 2,
    'Z' : 3,
}

# Get a list of every turn
turns = [
    [
        shapes[shape]
        for shape in turn.split(' ')
    ]
    for turn
    in text.split('\n')[:-1]
]


# Part 1
total = 0
for turn in turns:
    j1 = turn[1]
    j2 = turn[0]

    # Win
    if (j1 == 2 and j2 == 1) or (j1 == 3 and j2 == 2) or (j1 == 1 and j2 == 3):
        total += 6
    
    # Draw
    elif (j1 == j2):
        total += 3
    
    # Loose
    else:
        total += 0
        # Yes I know it's useless

    total += j1

print(f"Part 1 : {total}")


# Part 2
win   = {1:2, 2:3, 3:1}
draw  = {1:1, 2:2, 3:3}
loose = {1:3, 2:1, 3:2}

total = 0
for turn in turns:
    j2 = turn[0]
    end = turn[1]

    # j1 looses
    if (end == 1):
        total += loose[j2]
        total += 0

    # draw
    if (end == 2):
        total += draw[j2]
        total += 3

    # j1 win
    if (end == 3):
        total += win[j2]
        total += 6

print(f"Part 2 : {total}")
