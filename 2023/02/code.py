# Advent of Code 2023 - Day 2
# https://adventofcode.com/2023/day/2
# Author: Alexandre MALFREYT

import typing

with open('input.txt', 'r') as f:
    games = [line.strip() for line in f.readlines()]

# Example of games:
# games = [
#     "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
#     "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
#     "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
#     "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
#     "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
# ]

games = [game.split(': ')[1] for game in games] # Remove "Game XX : "
games = [game.split('; ') for game in games] # Split handfuls for each game
games = [[handful.split(', ') for handful in game] for game in games] # Split cubes colors for each handful
games = [[{cube.split(' ')[1]: int(cube.split(' ')[0]) for cube in handful} for handful in game] for game in games] # Create dict for each cube color
[[[handful.update({color: 0}) for color in ['blue', 'green', 'red'] if color not in handful.keys()] for handful in game] for game in games] # Add missing colors with 0 value

# Example of games:
# [[{'blue': 3, 'green': 0, 'red': 4}, {'blue': 6, 'green': 2, 'red': 1}, {'blue': 0, 'green': 2, 'red': 0}],
#  [{'blue': 1, 'green': 2, 'red': 0}, {'blue': 4, 'green': 3, 'red': 1}, {'blue': 1, 'green': 1, 'red': 0}],
#  [{'blue': 6, 'green': 8, 'red': 20}, {'blue': 5, 'green': 13, 'red': 4}, {'blue': 0, 'green': 5, 'red': 1}],
#  [{'blue': 6, 'green': 1, 'red': 3}, {'blue': 0, 'green': 3, 'red': 6}, {'blue': 15, 'green': 3, 'red': 14}],
#  [{'blue': 1, 'green': 3, 'red': 6}, {'blue': 2, 'green': 2, 'red': 1}]]

# Format: games[game][handful][color] = number_of_cubes

from pprint import pprint; pprint(games, width=200)

# Part 1
def is_game_possible(game: typing.List[typing.Dict[str, int]], bag: typing.Dict[str, int]) -> bool:
    """Check for each handful if there is enough cubes in the bag"""
    for handful in game:
        for color in handful.keys():
            if handful[color] > bag[color]:
                print(f'Not possible: {handful[color]} {color} cubes in handful, but only {bag[color]} in bag')
                return False
    return True

total = 0
for i in range(len(games)):
    game_id = i+1

    # is game possible with 12 red cubes, 13 green cubes, and 14 blue cubes in the bag?
    if is_game_possible(games[i], {'red': 12, 'green': 13, 'blue': 14}):
        total += game_id
        print(f'Game {game_id} is possible')
    else:
        print(f'Game {game_id} is not possible')

print(f'Part 1 : {total}')


# Part 2
def min_possible_bag(game: typing.List[typing.Dict[str, int]]) -> typing.Dict[str, int]:
    """Return the minimum number of cubes needed for each color to play the game"""
    bag = {'red': 0, 'green': 0, 'blue': 0}
    for handful in game:
        for color in handful.keys():
            if handful[color] > bag[color]:
                bag[color] = handful[color]
    return bag

def calulate_set_power(handful: typing.Dict[str, int]) -> typing.Dict[str, int]:
    """Return the power of a set of cubes"""
    power = 1
    for color in handful.keys():
        power *= handful[color]
        print(f'{handful[color]} {color} cubes in handful, power is now {power}')
    return power

total = 0
for i in range(len(games)):
    game_id = i+1
    total += calulate_set_power(min_possible_bag(games[i]))

print(f'Part 2 : {total}')
