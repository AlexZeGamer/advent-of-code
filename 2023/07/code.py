# Advent of Code 2023 - Day 7
# https://adventofcode.com/2023/day/7
# Author: Alexandre MALFREYT

from functools import cmp_to_key
import itertools

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
    
def compare_hands(hand1: List[str], hand2: List[str], f = hand_type) -> int:
    print(f'Comparing {hand1} and {hand2}') if DEBUG else None

    if type(hand1) != list or type(hand2) != list:
        raise TypeError(f'Hands must be lists (not {type(hand1)} and {type(hand2)})')

    if len(hand1) != len(hand2):
        raise ValueError('Hands must have the same length')
    
    if hand1 == hand2:
        return 0

    # First we compare the hand types
    if f(hand1) < f(hand2):
        print(f'{hand1} ({f(hand1)}) < {hand2} ({f(hand2)})') if DEBUG else None
        return -1
    elif f(hand1) > f(hand2):
        print(f'{hand1} ({f(hand1)}) > {hand2} ({f(hand2)})') if DEBUG else None
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
    return None

assert compare_hands(['3', '2', 'T', '3', 'K'], ['K', 'K', '6', '7', '7']) == -1
assert compare_hands(['K', 'K', '6', '7', '7'], ['K', 'T', 'J', 'J', 'T']) == 1
assert compare_hands(['T', '5', '5', 'J', '5'], ['Q', 'Q', 'Q', 'J', 'A']) == -1
assert compare_hands(['T', '5', '5', 'J', '5'], ['T', '5', '5', 'J', '5']) == 0
assert compare_hands(['T', '5', '5', 'J', '5'], ['T', '5', '5', 'J', '6']) == 1

# sort from lowest to highest power (compare_hands)
games_sorted = sorted(games, key=cmp_to_key(lambda x, y: compare_hands(x['hand'], y['hand'])))

print([''.join(game['hand']) for game in games]) if DEBUG else None
print([''.join(game['hand']) for game in games_sorted]) if DEBUG else None

total = 0
for i in range(len(games_sorted)):
    total += games_sorted[i]['bid'] * (i + 1)

print(f'Part 1: {total}')



# Part 2
possible_cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
possible_cards.reverse() # from lowest to highest

def hand_type_with_joker(hand: List[str]) -> int:
    hand = hand.copy()
    joker_indexes = [i for i, card in enumerate(hand) if card == 'J']
    max_type = 0

    it = itertools.product(possible_cards, repeat=len(joker_indexes))
    for cards in it:
        for i, card in enumerate(cards):
            hand[joker_indexes[i]] = card
        max_type = max(max_type, hand_type(hand))

    return max_type

assert hand_type_with_joker(['J', 'J', 'J', 'J', 'J']) == 7
assert hand_type_with_joker(['J', 'J', 'J', 'J', 'K']) == 7
assert hand_type_with_joker(['3', '2', 'T', '3', 'K']) == 2
assert hand_type_with_joker(['K', 'K', '6', '7', '7']) == 3
assert hand_type_with_joker(['T', '5', '5', 'J', '5']) == 6
assert hand_type_with_joker(['K', 'T', 'J', 'J', 'T']) == 6 
assert hand_type_with_joker(['Q', 'Q', 'Q', 'J', 'A']) == 6

# 32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
# KK677 is now the only two pair, making it the second-weakest hand.
# T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
assert compare_hands(['3', '2', 'T', '3', 'K'], ['K', 'K', '6', '7', '7'], hand_type_with_joker) == -1
assert compare_hands(['K', 'K', '6', '7', '7'], ['K', 'T', 'J', 'J', 'T'], hand_type_with_joker) == -1
assert compare_hands(['T', '5', '5', 'J', '5'], ['Q', 'Q', 'Q', 'J', 'A'], hand_type_with_joker) == -1
assert compare_hands(['T', '5', '5', 'J', '5'], ['T', '5', '5', 'J', '5'], hand_type_with_joker) == 0
assert compare_hands(['T', '5', '5', 'J', '5'], ['T', '5', '5', 'J', '6'], hand_type_with_joker) == 1

games_sorted = sorted(games, key=cmp_to_key(lambda x, y: compare_hands(x['hand'], y['hand'], hand_type_with_joker)))

print([''.join(game['hand']) for game in games_sorted]) if DEBUG else None
print([hand_type_with_joker(game['hand']) for game in games_sorted]) if DEBUG else None

total = 0
for i in range(len(games_sorted)):
    total += games_sorted[i]['bid'] * (i + 1)

print(f'Part 2: {total}')
