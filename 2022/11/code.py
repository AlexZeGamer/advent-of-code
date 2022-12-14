# Advent of Code 2022 - Day 11
# https://adventofcode.com/2022/day/11
# Author: Alexandre MALFREYT
from math import prod

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

### Example
# lines = """Monkey 0:
#   Starting items: 79, 98
#   Operation: new = old * 19
#   Test: divisible by 23
#     If true: throw to monkey 2
#     If false: throw to monkey 3

# Monkey 1:
#   Starting items: 54, 65, 75, 74
#   Operation: new = old + 6
#   Test: divisible by 19
#     If true: throw to monkey 2
#     If false: throw to monkey 0

# Monkey 2:
#   Starting items: 79, 60, 97
#   Operation: new = old * old
#   Test: divisible by 13
#     If true: throw to monkey 1
#     If false: throw to monkey 3

# Monkey 3:
#   Starting items: 74
#   Operation: new = old + 3
#   Test: divisible by 17
#     If true: throw to monkey 0
#     If false: throw to monkey 1
# """.splitlines()

def apply_operation(a:int, b:int, operation:str):
    """Apply operation to a and b"""
    if b == "old":
        b = a
    else:
        b = int(b)
    
    match operation:
        case "+":
            return a + b
        case "*":
            return a * b
        case "-":
            return a - b
        case "/":
            return a / b
        case other:
            raise Exception(f'Unknown operation {other}')

### Part 1
monkeys = []
for i in range(0, len(lines), 7):
    monkey = {}
    monkey['items'] = [int(elem) for elem in lines[i+1].replace("  Starting items: ", "").split(", ")]
    monkey['operation'] = lines[i+2].replace("  Operation: new = ", "").split(" ")[1:]
    monkey['test']  = int(lines[i+3].replace("  Test: ", "").split(" ")[-1])
    monkey['true']  = int(lines[i+4].replace("    If true: throw to monkey ", "")[-1])
    monkey['false'] = int(lines[i+5].replace("    If false: throw to monkey ", "")[-1])
    monkey['count'] = 0
    monkeys.append(monkey)

# Rounds
for round in range(20):
    # Monkeys
    for monkey in monkeys:
        # Items
        for _ in range(len(monkey['items'])):
            monkey['count'] += 1

            # apply operation
            monkey['items'][0] = apply_operation(monkey['items'][0], monkey['operation'][1], monkey['operation'][0])
            
            # monkey gets bored
            monkey['items'][0] //= 3

            # test
            if not monkey['items'][0] % monkey['test']:
                monkeys[monkey['true']]['items'].append(monkey['items'][0])
            else:
                monkeys[monkey['false']]['items'].append(monkey['items'][0])
            monkey['items'].remove(monkey['items'][0])
    
print(f'Round {round+1}')
for i, monkey in enumerate(monkeys):
    print(f'Monkey {i} : {monkey["items"]} ({monkey["count"]})')

print(f'Part 1 : {prod(sorted([monkey["count"] for monkey in monkeys])[-2:])}')

