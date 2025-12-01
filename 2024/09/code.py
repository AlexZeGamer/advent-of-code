# Advent of Code 2024 - Day 9
# https://adventofcode.com/2024/day/9
# Author: Alexandre MALFREYT

DEBUG = True

with open('input.txt', 'r') as f:
    disk_map = f.read().strip()

disk_map = "2333133121414131402"    # Example 1
# disk_map = "12345"                  # Example 2

data = [int(e) for e in disk_map[::2]]            # Data is on even indexes
empty_space = [int(e) for e in disk_map[1::2]]    # Empty space is on odd indexes

# print(f'Data : {data}') if DEBUG else None
# print(f'Empty space : {empty_space}') if DEBUG else None

def print_visu(data, empty_space):
    disk = zip(data, empty_space)
    visu = ""
    file_id = 0
    for d, e in disk:
        if d is not None:
            visu += str(file_id)*d
        if e is not None:
            visu += "."*e
        file_id += 1
    return visu

# Part 1 (optimized)
data_p1 = data.copy()
empty_space_p1 = empty_space.copy()

total = 0

cursor = 0          # Current position on disk (block number)
file_id = 0         # Current position in the data or empty_space string
data_flag = True    # whether we are in data or empty_space
# while True:
#     print("----------------------------------------------") if DEBUG else None
#     if data_flag:
#         # print "Reading data" in yellow
#         print(f'\033[33mReading data\033[0m') if DEBUG else None

#     else:
#         # print "Filling empty space" in green
#         print(f'\033[32mFilling empty space\033[0m') if DEBUG else None
#     print(f'Current position in disk : {cursor}') if DEBUG else None
#     print(f'Current file id : {file_id}') if DEBUG else None

#     if data_p1[-1] == 0: # If the last file is empty, it has been moved entirely to fill empty space
#             data_p1.pop()      # so we can remove it

#     if all(e == 0 for e in data_p1):
#         print(f'All data is read') if DEBUG else None
#         break

#     # Read the current file
#     if data_flag:
#         # If we reached EOF, switch to empty_space
#         if data_p1[file_id] == 0:
#             data_flag = False
#             print(f'EOF, switching to empty space') if DEBUG else None
#             continue

#         # If we are not at the EOF, add i*file_id to the total
#         total += cursor*file_id
#         print(f'{cursor} * {file_id} = {cursor*file_id}') if DEBUG else None
#         data_p1[file_id] -= 1

#     # Fill the empty space with data
#     else:
#         # If we reached EOF, switch to data
#         if empty_space_p1[file_id] == 0:
#             data_flag = True
#             file_id += 1
#             print(f'EOF, switching to data') if DEBUG else None
#             continue

#         # If we are not at the EOF, fill the empty space with the data from the last file
#         total += cursor*(len(data_p1)-1)
#         print(f'{cursor} * {len(data_p1)-1} = {cursor*(len(data_p1)-1)}') if DEBUG else None
#         data_p1[-1] -= 1
#         empty_space_p1[file_id] -= 1

#     print(f"Data : {data_p1}") if DEBUG else None
#     print(f"Empty space : {empty_space_p1}") if DEBUG else None
#     print(f'Total : {total}') if DEBUG else None
#     cursor+=1

print(f'Part 1 : {total}')


# Part 2
data_p2 = data.copy()
empty_space_p2 = empty_space.copy()

total = 0

cursor = 0          # Current position on disk (block number)
file_id = 0         # Current position in the data or empty_space string
data_flag = True    # whether we are in data or empty_space
while True:
    print("Data : ", data_p2) if DEBUG else None
    print("Empty space : ", empty_space_p2) if DEBUG else None
    print(f"Visu : {print_visu(data_p2, empty_space_p2)}") if DEBUG else None
    print(f'Current position in disk : {cursor}') if DEBUG else None
    print(f'Current file id : {file_id}') if DEBUG else None
    print(f'Total : {total}') if DEBUG else None
    print("----------------------------------------------") if DEBUG else None
    if data_flag:
        print(f'\033[33mReading data\033[0m') if DEBUG else None
    else:
        print(f'\033[32mFilling empty space\033[0m') if DEBUG else None
    
    if all(e is None for e in data_p2):
        print(f'All data is read') if DEBUG else None
        break

    # Read the current file
    if data_flag:
        # skip empty files
        if data_p2[file_id] is None:
            file_id += 1
            continue

        print(f'data_p2[{file_id}] = {data_p2[file_id]}') if DEBUG else None
        for i in range(data_p2[file_id]):
            print(f'\033[31mAdding {cursor} * {file_id} = {cursor*file_id} to total\033[0m') if DEBUG else None
            total += cursor*file_id
            cursor += 1
        data_p2[file_id] = None
        data_flag = False

    # Fill the empty space with data
    else:
        # find the first file in data that fits in the empty space starting from the end
        file_to_move_id = None
        for i in range(len(data_p2)-1, -1, -1):
            if data_p2[i] is not None and data_p2[i] <= empty_space_p2[file_id]:
                file_to_move_id = i
                print(f'File {file_to_move_id} fits in empty space {file_id}') if DEBUG else None
                break

        # if no file fits, switch back to data
        if file_to_move_id is None:
            print(f'No file fits in empty space {file_id}, switching back to data') if DEBUG else None
            data_flag = True
            continue

        # read the file as being moved to the empty space and delete it from data (set it to None)
        print(f"empty_space_p2[{file_id}] = {empty_space_p2[file_id]}") if DEBUG else None
        for i in range(data[file_to_move_id]):
            print(f'\033[31mAdding {cursor} * {file_to_move_id} = {cursor*file_to_move_id} to total\033[0m') if DEBUG else None
            total += cursor*file_to_move_id
            empty_space_p2[file_id] -= 1
            cursor += 1
        data_p2[file_to_move_id] = None
        if empty_space_p2[file_id] == 0:
            empty_space_p2[file_id] = None
            file_id += 1
            data_flag = True

print(f'Part 2 : {total}')
