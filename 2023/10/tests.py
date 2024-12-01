from code import find_start, get_path, predict_pipe, get_farthest_point_distance, get_number_of_tiles_in_loop

# Examples
example1 = [
    ['-','L','|','F','7'],
    ['7','S','-','7','|'],
    ['L','|','7','|','|'],
    ['-','L','-','J','|'],
    ['L','|','-','J','F']
]

example2 = [
    ['7','-','F','7','-'],
    ['.','F','J','|','7'],
    ['S','J','L','L','7'],
    ['|','F','-','-','J'],
    ['L','J','.','L','J']
]

example3 = [
    ['.','.','.','.','.','.','.','.','.','.','.'],
    ['.','S','-','-','-','-','-','-','-','7','.'],
    ['.','|','F','-','-','-','-','-','7','|','.'],
    ['.','|','|','.','.','.','.','.','|','|','.'],
    ['.','|','|','.','.','.','.','.','|','|','.'],
    ['.','|','L','-','7','.','F','-','J','|','.'],
    ['.','|','.','.','|','.','|','.','.','|','.'],
    ['.','L','-','-','J','.','L','-','-','J','.'],
    ['.','.','.','.','.','.','.','.','.','.','.'],
]

example4 = [
    ['.','.','.','.','.','.','.','.','.','.'],
    ['.','S','-','-','-','-','-','-','7','.'],
    ['.','|','F','-','-','-','-','7','|','.'],
    ['.','|','|','.','.','.','.','|','|','.'],
    ['.','|','|','.','.','.','.','|','|','.'],
    ['.','|','L','-','7','F','-','J','|','.'],
    ['.','|','.','.','|','|','.','.','|','.'],
    ['.','L','-','-','J','L','-','-','J','.'],
    ['.','.','.','.','.','.','.','.','.','.'],
]

example5 = [
    ['.','F','-','-','-','-','7','F','7','F','7','F','7','F','-','7','.','.','.','.'],
    ['.','|','F','-','-','7','|','|','|','|','|','|','|','|','F','J','.','.','.','.'],
    ['.','|','|','.','F','J','|','|','|','|','|','|','|','|','L','7','.','.','.','.'],
    ['F','J','L','7','L','7','L','J','L','J','|','|','L','J','.','L','-','7','.','.'],
    ['L','-','-','J','.','L','7','.','.','.','L','J','S','7','F','-','7','L','7','.'],
    ['.','.','.','.','F','-','J','.','.','F','7','F','J','|','L','7','L','7','L','7'],
    ['.','.','.','.','L','7','.','F','7','|','|','L','7','|','.','L','7','L','7','|'],
    ['.','.','.','.','.','|','F','J','L','J','|','F','J','|','F','7','|','.','L','J'],
    ['.','.','.','.','F','J','L','-','7','.','|','|','.','|','|','|','|','.','.','.'],
    ['.','.','.','.','L','-','-','-','J','.','L','J','.','L','J','L','J','.','.','.'],
]

example6 = [
    ['F','F','7','F','S','F','7','F','7','F','7','F','7','F','7','F','-','-','-','7'],
    ['L','|','L','J','|','|','|','|','|','|','|','|','|','|','|','|','F','-','-','J'],
    ['F','L','-','7','L','J','L','J','|','|','|','|','|','|','L','J','L','-','7','7'],
    ['F','-','-','J','F','-','-','7','|','|','L','J','L','J','7','F','7','F','J','-'],
    ['L','-','-','-','J','F','-','J','L','J','.','|','|','-','F','J','L','J','J','7'],
    ['|','F','|','F','-','J','F','-','-','-','7','F','7','-','L','7','L','|','7','|'],
    ['|','F','F','J','F','7','L','7','F','-','J','F','7','|','J','L','-','-','-','7'],
    ['7','-','L','-','J','L','7','|','|','F','7','|','L','7','F','-','7','F','7','|'],
    ['L','.','L','7','L','F','J','|','|','|','|','|','F','J','L','7','|','|','L','J'],
    ['L','7','J','L','J','L','-','J','L','J','L','J','L','-','-','J','L','J','.','L'],
]


# Tests
start_poses = []
paths = []
for e in [example1, example2, example3, example4, example5, example6]:
    # Replace start with the correct pipe
    start_pos = find_start(e)
    start_poses.append(start_pos)
    e[start_pos[0]][start_pos[1]] = predict_pipe(e, start_pos)

    # Get path
    path = get_path(e, start_pos)
    paths.append(path)

assert start_poses[0] == (1, 1)
assert start_poses[1] == (2, 0)
assert start_poses[2] == (1, 1)
assert start_poses[3] == (1, 1)
assert start_poses[4] == (4, 12)
assert start_poses[5] == (0, 4)

assert predict_pipe(example1, start_poses[0]) == 'F'
assert predict_pipe(example2, start_poses[1]) == 'F'
assert predict_pipe(example3, start_poses[2]) == 'F'
assert predict_pipe(example4, start_poses[3]) == 'F'
assert predict_pipe(example5, start_poses[4]) == 'F'
assert predict_pipe(example6, start_poses[5]) == '7'

assert get_farthest_point_distance(get_path(example1, start_poses[0])) == 4
assert get_farthest_point_distance(get_path(example2, start_poses[1])) == 8

assert get_number_of_tiles_in_loop(example1, paths[0]) == 1
assert get_number_of_tiles_in_loop(example2, paths[1]) == 1
assert get_number_of_tiles_in_loop(example3, paths[2]) == 4
assert get_number_of_tiles_in_loop(example4, paths[3]) == 4
assert get_number_of_tiles_in_loop(example5, paths[4]) == 8
assert get_number_of_tiles_in_loop(example6, paths[5]) == 10

print("All tests passed successfully!")
