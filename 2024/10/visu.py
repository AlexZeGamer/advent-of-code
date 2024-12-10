# Visualizations for the Advent of Code 2024 Day 10 challenge
import matplotlib.pyplot as plt

with open("input.txt", "r") as f:
    map = [[x for x in y.strip()] for y in f.readlines()]

# Example
map = [
    [8, 9, 0, 1, 0, 1, 2, 3],
    [7, 8, 1, 2, 1, 8, 7, 4],
    [8, 7, 4, 3, 0, 9, 6, 5],
    [9, 6, 5, 4, 9, 8, 7, 4],
    [4, 5, 6, 7, 8, 9, 0, 3],
    [3, 2, 0, 1, 9, 0, 1, 2],
    [0, 1, 3, 2, 9, 8, 0, 1],
    [1, 0, 4, 5, 6, 7, 3, 2],
]

# Visualize the grid (colors from 0 et 9)
def visu_plot(map):
    """
    Visualize the grid with colors for values from 0 to 9 (from blue to red)
    """
    fig, ax = plt.subplots()
    ax.imshow([[int(x) for x in y] for y in map])
    plt.show()

#######################################################################################

visu_plot(map)
