# Advent of Code 2023 - Day 7
# https://adventofcode.com/2023/day/7
# Author: Alexandre MALFREYT

from functools import cmp_to_key
from typing import List, Dict

DEBUG = False

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Example
# lines = ['32T3K 765', 'T55J5 684', 'KK677 28', 'KTJJT 220', 'QQQJA 483']
    
games = [
    {
        'hand': [card for card in line.split(' ')[0]],
        'bid' : int(line.split(' ')[1]),
    }
    for line in lines
]
print(games) if DEBUG else None

# Part 1
possible_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
possible_cards.reverse() # from lowest to highest

hand_types = ['High card', 'One pair', 'Two pairs', 'Three of a kind', 'Straight', 'Flush', 'Full house', 'Four of a kind', 'Straight flush', 'Five of a kind']

def repartition(hand: List[str]) -> Dict[str, int]:
    return {card: hand.count(card) for card in hand}

def hand_type(hand: List[str]) -> int:
    if len(hand) != 5:
        raise ValueError(f'Hand must contain 5 cards (not {len(hand)})')

    rep = repartition(hand)
    cards_frequency = list(rep.values())

    # Five of a kind
    if 5 in cards_frequency:
        return 7
    
    # Four of a kind
    elif 4 in cards_frequency:
        return 6
    
    # Full house
    elif 3 in cards_frequency and 2 in cards_frequency:
        return 5
    
    # Three of a kind
    elif 3 in cards_frequency:
        return 4
    
    # Two pairs
    elif cards_frequency.count(2) == 2:
        return 3
    
    # One pair
    elif 2 in cards_frequency:
        return 2
    
    # High card
    else:
        return 1
    
def compare_hands(hand1: List[str], hand2: List[str]) -> int:
    print(f'Comparing {hand1} and {hand2}') if DEBUG else None

    if type(hand1) != list or type(hand2) != list:
        raise TypeError(f'Hands must be lists (not {type(hand1)} and {type(hand2)})')

    if len(hand1) != len(hand2):
        raise ValueError('Hands must have the same length')
    
    if hand1 == hand2:
        return 0

    # First we compare the hand types
    if hand_type(hand1) < hand_type(hand2):
        print(f'{hand1} ({hand_type(hand1)}) < {hand2} ({hand_type(hand2)})') if DEBUG else None
        return -1
    elif hand_type(hand1) > hand_type(hand2):
        print(f'{hand1} ({hand_type(hand1)}) > {hand2} ({hand_type(hand2)})') if DEBUG else None
        return 1
    
    #If the hand types are the same, we compare the cards one by one
    else:
        for i in range(len(hand1)):
            if possible_cards.index(hand1[i]) < possible_cards.index(hand2[i]):
                print(f'{hand1} < {hand2} because {hand1[i]} < {hand2[i]}') if DEBUG else None
                return -1
            elif possible_cards.index(hand1[i]) > possible_cards.index(hand2[i]):
                print(f'{hand1} > {hand2} because {hand1[i]} > {hand2[i]}') if DEBUG else None
                return 1

# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
# KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.

assert compare_hands(['3', '2', 'T', '3', 'K'], ['K', 'K', '6', '7', '7']) == -1
assert compare_hands(['K', 'K', '6', '7', '7'], ['K', 'T', 'J', 'J', 'T']) == 1
assert compare_hands(['T', '5', '5', 'J', '5'], ['Q', 'Q', 'Q', 'J', 'A']) == -1
assert compare_hands(['T', '5', '5', 'J', '5'], ['T', '5', '5', 'J', '5']) == 0
assert compare_hands(['T', '5', '5', 'J', '5'], ['T', '5', '5', 'J', '6']) == 1

# sort from lowest to highest power (compare_hands)
# games.sort(key=cmp_to_key(lambda x, y: compare_hands(x['hand'], y['hand'])))

games_sorted = sorted(games, key=cmp_to_key(lambda x, y: compare_hands(x['hand'], y['hand'])))

print([''.join(game['hand']) for game in games]) if DEBUG else None
print([''.join(game['hand']) for game in games_sorted]) if DEBUG else None

total = 0
for i in range(len(games_sorted)):
    total += games_sorted[i]['bid'] * (i + 1)

print(f'Part 1: {total}')

# Part 2
total = 0

print(f'Part 2: {total}')