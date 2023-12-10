from typing import List, Tuple
from functions import is_in_loop

LARGE_VIEW = True

if LARGE_VIEW:
    repr = {'|': '║ ', '-': '══', 'L': '╚═', 'J': '╝ ', '7': '╗ ', 'F': '╔═', '.': '  ', 'S': '██'}
else:
    repr = {'|': '║', '-': '═', 'L': '╚', 'J': '╝', '7': '╗', 'F': '╔', '.': ' ', 'S': '█'}

# Visualisation functions
def visu_color(maze: List[List[str]], path: List[Tuple[int, int]], show_inside: bool = False) -> None:
    """Visualize the maze with the path with a color gradient and a dark gray background"""
    colors = ['\033[34m', '\033[94m', '\033[36m', '\033[96m', '\033[32m', '\033[92m', '\033[93m', '\033[33m', '\033[91m', '\033[31m', '\033[35m', '\033[95m']

    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            color = '\033[90m' # Default color for background (dark gray)
            color = colors[int((path.index((i,j)) / len(path)) * len(colors))] if (i,j) in path else color # Color gradient for path
            if show_inside:
                color = '\033[97m' if is_in_loop((i,j), path, maze) else color # White for tiles in the loop
            
            print(color, end='')
            print(repr[c], end='')
            print('\033[0m', end='')
        print()

def visu_green(maze: List[List[str]], path: List[Tuple[int, int]], show_inside: bool = False) -> None:
    """Visualize the maze with the path in green and a dark gray background"""
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            color = '\033[92m' if (i,j) in path else '\033[90m'
            if show_inside:
                color = '\033[97m' if is_in_loop((i,j), path, maze) else color

            print(color, end='')
            print(repr[c], end='')
            print('\033[0m', end='')
        print()

def visu_BandW(maze: List[List[str]]) -> None:
    """Visualize the maze in black and white"""
    for line in maze:
        for c in line:
            print(repr[c], end='')
        print()
