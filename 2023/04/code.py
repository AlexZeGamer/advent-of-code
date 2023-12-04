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

cards_str = '\n'.join([
    "Card " + str(i+1).rjust(3) + ": "
    + ' '.join(str(c).rjust(2) for c in card['winning_numbers'])
    + " | "
    + ' '.join(str(c).rjust(2) for c in card['numbers_you_have'])
    for i, card in enumerate(cards)
]) + '\n'
print(cards_str == text) if DEBUG else None
print(len(cards_str), len(text)) if DEBUG else None
print(cards_str[:10] + '|', text[:10] + '|') if DEBUG else None

# Example
cards = [
    {"winning_numbers": [41, 48, 83, 86, 17], "numbers_you_have": [83, 86,  6, 31, 17,  9, 48, 53]},
    {"winning_numbers": [13, 32, 20, 16, 61], "numbers_you_have": [61, 30, 68, 82, 17, 32, 24, 19]},
    {"winning_numbers": [ 1, 21, 53, 59, 44], "numbers_you_have": [69, 82, 63, 72, 16, 21, 14,  1]},
    {"winning_numbers": [41, 92, 73, 84, 69], "numbers_you_have": [59, 84, 76, 51, 58,  5, 54, 83]},
    {"winning_numbers": [87, 83, 26, 28, 32], "numbers_you_have": [88, 30, 70, 12, 93, 22, 82, 36]},
    {"winning_numbers": [31, 18, 13, 56, 72], "numbers_you_have": [74, 77, 10, 23, 35, 67, 36, 11]},
]

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

def number_of_winning_numbers_in_card(card):
    count = 0
    for number in card['numbers_you_have']:
        if number in card['winning_numbers']:
            count += 1
    return count

# cards_in_hand = cards[:] # copy
cards_in_hand_indices = [i for i in range(len(cards))]
# print(cards_in_hand_indices) if DEBUG else None

i = 0
while i < len(cards_in_hand_indices):
    # n = number_of_winning_numbers_in_card(cards_in_hand[i])
    n = number_of_winning_numbers_in_card(cards[cards_in_hand_indices[i]])
    for j in range(n, 0, -1):
        # print(cards.index(cards_in_hand[i])+j, j)
        # index = cards.index(cards_in_hand[i])+j
        index = cards_in_hand_indices[i]+j
        if index >= len(cards):
            break
        # card_to_add = cards[index]

        # print(cards_in_hand.index(cards_in_hand[i+j]), index) if DEBUG else None
        # cards_in_hand.insert(cards_in_hand.index(cards_in_hand[i+j]), card_to_add)
        # cards_in_hand_indices.insert(cards_in_hand.index(cards_in_hand[i+j]), index)
        # print(i+j+1, index) if DEBUG else None
        # cards_in_hand.insert(cards_in_hand.index(card_to_add), card_to_add)
        cards_in_hand_indices.insert(cards_in_hand_indices.index(index), index)

        print(cards_in_hand_indices) if DEBUG else None
    print(f"Tour n°{i+1} : {n} cartes ajoutées, {len(cards_in_hand_indices)} cartes en main") if DEBUG and not i%1000 else None
    i += 1

print(f'Part 2 : {len(cards_in_hand_indices)}')