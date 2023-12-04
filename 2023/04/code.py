# Advent of Code 2023 - Day 4
# https://adventofcode.com/2023/day/4
# Author: Alexandre MALFREYT

DEBUG = True

with open('input.txt', 'r') as f:
    text = f.read()
    f.seek(0)
    cards = [line.strip() for line in f.readlines()]

cards = [card.split(': ')[1] for card in cards]
cards = [card.split(' | ') for card in cards]
cards = [
    {
        'winning_numbers': [int(number) for number in card[0].split()],
        'numbers_you_have': [int(number) for number in card[1].split()]
    }
    for card in cards
]

# Example
# cards = [
#     {"winning_numbers": [41, 48, 83, 86, 17], "numbers_you_have": [83, 86,  6, 31, 17,  9, 48, 53]},
#     {"winning_numbers": [13, 32, 20, 16, 61], "numbers_you_have": [61, 30, 68, 82, 17, 32, 24, 19]},
#     {"winning_numbers": [ 1, 21, 53, 59, 44], "numbers_you_have": [69, 82, 63, 72, 16, 21, 14,  1]},
#     {"winning_numbers": [41, 92, 73, 84, 69], "numbers_you_have": [59, 84, 76, 51, 58,  5, 54, 83]},
#     {"winning_numbers": [87, 83, 26, 28, 32], "numbers_you_have": [88, 30, 70, 12, 93, 22, 82, 36]},
#     {"winning_numbers": [31, 18, 13, 56, 72], "numbers_you_have": [74, 77, 10, 23, 35, 67, 36, 11]},
# ]

# Part 1
total = 0

for card in cards:
    points = 0
    for number in card['numbers_you_have']:
        if number in card['winning_numbers']:
            if points == 0:
                points = 1
            else:
                points *= 2
    total += points

print(f'Part 1 : {total}')


# Part 2
total = 0

memory = {}

def number_of_winning_numbers_in_card(card_id):
    if card_id in memory:
        return memory[card_id]
    
    card = cards[card_id]
    count = 0
    for number in card['numbers_you_have']:
        if number in card['winning_numbers']:
            count += 1

    memory[card_id] = count
    return count

def number_of_cards_remaining(number_of_each_card):
    return sum(number_of_each_card)

def next_card_to_check(number_of_each_card, i):
    total = 0
    for j in range(len(number_of_each_card)):
        total += number_of_each_card[j]
        if total > i:
            return j
    return None

number_of_each_card = [1] * len(cards)
card_id = 0
i = 0
while True:
    card_id = next_card_to_check(number_of_each_card, i)
    if card_id is None:
        break
    n = number_of_winning_numbers_in_card(card_id)

    for j in range(1, n+1):
        copy_id = card_id + j
        number_of_each_card[copy_id] += 1

    print(f"Tour n°{i+1} : Carte n°{card_id}, {n} cartes ajoutées, {sum(number_of_each_card)} cartes en main") if DEBUG and not i % 100000 else None
    i += 1

print(f'Part 2 : {sum(number_of_each_card)}')
