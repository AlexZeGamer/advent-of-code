# Advent of Code 2022 - Day 25
# https://adventofcode.com/2022/day/25
# Author: Alexandre MALFREYT

import itertools

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# Example
lines = [
"1=-0-2", # 1747
 "12111", # 906
  "2=0=", # 198
    "21", # 11
  "2=01", # 201
   "111", # 31
 "20012", # 1257
   "112", # 32
 "1=-1=", # 353
  "1-12", # 107
    "12", # 7
    "1=", # 3
   "122", # 37
]

# Part 1
total = 0

def dec_to_snafu(input: int) -> str:
    # TODO
    return ''

def snafu_to_dec(input: str):
    snafu_code = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

    power = 1
    output = 0
    for i in range(len(input)-1, -1, -1):
        output += snafu_code[input[i]] * power
        power *= 5
    return output

print(snafu_to_dec('2=-01'))
print(dec_to_snafu(1250))
# for line in lines:
#     print(line, snafu_to_dec(line), total)
#     print()
#     total += snafu_to_dec(line)

print(f'Part 1 : {total}')


# Part 2
total = 0



print(f'Part 2 : {total}')
