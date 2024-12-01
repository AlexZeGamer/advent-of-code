from time import sleep
from typing import List, Tuple

possible_pipes = {
        '|': ['up', 'down'],
        '-': ['left', 'right'],
        'L': ['up', 'right'],
        'J': ['up', 'left'],
        '7': ['left', 'down'],
        'F': ['right', 'down'],
    }

# Functions for part 1
def find_start(maze: List[List[str]]) -> Tuple[int, int]:
    """Find the start position in the maze"""
    for i, line in enumerate(maze):
        for j, c in enumerate(line):
            if c == 'S':
                return (i,j)


def predict_pipe(maze: List[List[str]], pos: Tuple[int, int]) -> str:
    """Predict the pipe at a given position in the maze"""
    directions = {'up': (pos[0]-1, pos[1]), 'down': (pos[0]+1, pos[1]), 'left': (pos[0], pos[1]-1), 'right': (pos[0], pos[1]+1)}

    # Check every possible pipe and return the first one that fits
    for pipe in possible_pipes:
        pipe_fits = True

        # Check if the current pipe fits with the pipes around it
        for i, dir in enumerate(possible_pipes[pipe]):
            fits = False
            if dir == 'up' and directions['up'][0] >= 0:
                fits = are_pipes_connectable_vertical(maze[directions['up'][0]][directions['up'][1]], pipe) or fits
            if dir == 'down' and directions['down'][0] < len(maze):
                fits = are_pipes_connectable_vertical(pipe, maze[directions['down'][0]][directions['down'][1]]) or fits
            if dir == 'left' and directions['left'][1] >= 0:
                fits = are_pipes_connectable_horizontal(maze[directions['left'][0]][directions['left'][1]], pipe) or fits
            if dir == 'right' and directions['right'][1] < len(maze[0]):
                fits = are_pipes_connectable_horizontal(pipe, maze[directions['right'][0]][directions['right'][1]]) or fits
            pipe_fits = fits and pipe_fits

        # Return the first pipe that fits
        if pipe_fits:
            return pipe


def are_pipes_connectable_vertical(up: str, down: str) -> bool:
    """Check if two pipes are connectable vertically"""
    possible_up = [p for p in possible_pipes if 'down' in possible_pipes[p]]
    possible_down = [p for p in possible_pipes if 'up' in possible_pipes[p]]
    return up in possible_up and down in possible_down

def are_pipes_connectable_horizontal(left: str, right: str) -> bool:
    """Check if two pipes are connectable horizontally"""
    possible_left = [p for p in possible_pipes if 'right' in possible_pipes[p]]
    possible_right = [p for p in possible_pipes if 'left' in possible_pipes[p]]
    return left in possible_left and right in possible_right
    
def is_connected(maze: List[List[str]], pos1: Tuple[int, int], pos2: Tuple[int, int]) -> bool:
    """Check if two positions of the maze are connected with a pipe"""

    # Same line (x)
    if pos1[0] == pos2[0]:
        left_pos, right_pos = sorted([pos1, pos2], key=lambda pos: pos[1])
        return are_pipes_connectable_horizontal(maze[left_pos[0]][left_pos[1]], maze[right_pos[0]][right_pos[1]])

    # Same column (y)
    if pos1[1] == pos2[1]:
        up_pos, down_pos = sorted([pos1, pos2], key=lambda pos: pos[0])
        return are_pipes_connectable_vertical(maze[up_pos[0]][up_pos[1]], maze[down_pos[0]][down_pos[1]])
    
    # Not connected
    return False


def next_pos(maze: List[List[str]], pos: Tuple[int, int], prev: Tuple[int, int]) -> Tuple[int, int]:
    """Find the next position in the maze from the current position (avoid going back)"""

    x, y = pos
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        # Same as previous
        if (x+dx, y+dy) == prev:
            continue
        
        # Out of bounds
        if x+dx < 0 or x+dx >= len(maze) or y+dy < 0 or y+dy >= len(maze[0]):
            continue

        if is_connected(maze, pos, (x+dx, y+dy)):
            return (x+dx, y+dy)


def get_path(maze: List[List[str]], start: Tuple[int, int]) -> List[Tuple[int, int]]:
    """Find the path in the maze (loop from start to start)"""

    # Find start position and initialize path
    pos = start
    path = [start]

    # Loop until we find the start position again
    while pos != start or len(path) <= 1:
        prev = path[-2] if len(path) > 1 else None
        pos = next_pos(maze, pos, prev)
        path.append(pos)
        
    return path


def get_farthest_point_distance(path: List[Tuple[int, int]]) -> int:
    return len(path)//2


# Functions for part 2

# NOT OPTIMIZED
def is_in_loop(pos: Tuple[int, int], path: List[Tuple[int, int]], maze: List[List[str]]) -> bool:
    """
    Check if a tile of the maze is closed inside the loop formed by the path using the ray casting algorithm.
    
    The ray casting algorithm is a method for determining the inclusion of a point of a polygon by casting a ray
    from the point to infinity in any direction and counting the number of times the ray crosses the edge of polygon.
    
    - If the point is on the outside of the polygon the ray will cross its edge an even number of times.
    - If the point is on the inside of the polygon then it will cross the edge an odd number of times.
    """
    if pos in path:
        return False
    
    x, y = pos

    vertical_pipes = ['|', 'L', 'J']
    horizontal_pipes = ['-', 'F', 'L']

    ray_up = [(i, y) for i in range(len(maze[:x])) if maze[i][y] in horizontal_pipes and (i,y) in path]
    ray_down = [(i, y) for i in range(x+1, len(maze)) if maze[i][y] in horizontal_pipes and (i,y) in path]
    ray_left = [(x, i) for i in range(len(maze[0][:y])) if maze[x][i] in vertical_pipes and (x,i) in path]
    ray_right = [(x, i) for i in range(y+1, len(maze[0])) if maze[x][i] in vertical_pipes and (x,i) in path]
    rays = [ray_up, ray_down, ray_left, ray_right]

    return all([len(ray) % 2 == 1 for ray in rays])

def get_number_of_tiles_in_loop(maze: List[List[str]], path: List[Tuple[int, int]]) -> int:
    """Count the number of tiles in the loop formed by the path"""
    total = 0
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if is_in_loop((i,j), path, maze):
                total += 1
    return total
