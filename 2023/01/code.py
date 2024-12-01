# Advent of Code 2023 - Day 1
# https://adventofcode.com/2023/day/1
# Author: Alexandre MALFREYT

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

# lines = [
#     "1abc2",
#     "pqr3stu8vwx",
#     "a1b2c3d4e5f",
#     "treb7uchet",
# ]

# Part 1
total = 0

for line in lines:
    first = None
    last = None
    for char in line:
        if char >= '0' and char <= '9':
            if first is None:
                first = char
            last = char
    total += int(first+last)

print(f'Part 1 : {total}')


# Part 2
# lines = [
#     "two1nine",
#     "eightwothree",
#     "abcone2threexyz",
#     "xtwone3four",
#     "4nineeightseven2",
#     "zoneight234",
#     "7pqrstsixteen",
# ]

digit_words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def check_if_word_at_pos(line, pos, word):
    # if the word is too long to fit in the line, return False
    if pos + len(word) > len(line):
        return False
    
    # make a string from line[i] to line[i+len(word)]
    # and check if it matches the word
    return line[pos:pos+len(word)] == word

assert check_if_word_at_pos("onetwothree", 0, "one") == True
assert check_if_word_at_pos("onetwothree", 3, "two") == True
assert check_if_word_at_pos("onetwothree", 6, "three") == True
assert check_if_word_at_pos("onetwothree", 1, "one") == False
assert check_if_word_at_pos("onetwothree", 0, "four") == False

total = 0
res_by_line = []

for line in lines:
    first = None
    last = None
    for i in range(len(line)):
        c = line[i]
        if c >= '0' and c <= '9':
            if first is None:
                first = c
            last = c
        else:
            for word, digit in digit_words.items():
                if check_if_word_at_pos(line, i, word):
                    if first is None:
                        first = digit
                    last = digit

    res_by_line.append(first+last)
    total += int(first+last)

print(f'Part 2 : {total}')

with open('output.txt', 'w') as f:
    f.write('\n'.join(res_by_line))