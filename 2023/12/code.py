# Advent of Code 2023 - Day 12
# https://adventofcode.com/2023/day/12
# Author: Alexandre MALFREYT

import pycosat as sat
import itertools as it


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

lines = [
    {
        "map": line.split(" ")[0],
        "groups": tuple(int(n) for n in line.split(" ")[1].split(",")),
    }
    for line in lines
]


# Part 1
def build_cnf(line):
    # create cnf by adding every constraint
    cnf = []
    cnf += set_known_damaged_spings(line["map"])
    # cnf += set_known_groups(line['map'], line["groups"])
    return cnf


# constraints
def set_known_damaged_spings(map):
    cnf = []
    print(map)
    for i, c in enumerate(map):
        print(i, c)
        if c == "#":
            cnf.append([i + 1])
        elif c == ".":
            cnf.append([-i + 1])
    return cnf


# ..... 3
# (1*2*3)+(2*3*4)+(3*4*5)
# -(-(1*2*3)*-(2*3*4)*-(3*4*5))
# -((-1+-2+-3)*(-2+-3+-4)*(-3+-4+-5))
# -()
def set_known_groups(map, groups):
    cnf = []
    # TODO

    return cnf


total = 0

print(lines[:5])
cnf = build_cnf(lines[0])
print(cnf)
sols = sat.itersolve(cnf)
for sol in sols:
    print(sol)
    total += 1

print(f"Part 1 : {total}")


# Part 2
total = 0


print(f"Part 2 : {total}")
