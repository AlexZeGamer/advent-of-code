# https://adventofcode.com/2022/day/1

with open('./input.txt', 'r') as f:
    text = f.read()

deers = [
    sum([
        int(cal)
        for cal in deer.split('\n')
        if cal != ''
    ])
    for deer in text.split('\n\n')
]

# Part 1
max_calories = max(deers)
print(f'Part 1 : {max_calories}')

# Part 2
sum_of_top3_calories = sum(sorted(deers)[-3:])
print(f'Part 2 : {sum_of_top3_calories}')
