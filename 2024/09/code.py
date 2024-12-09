# Advent of Code 2024 - Day 9
# https://adventofcode.com/2024/day/9
# Author: Alexandre MALFREYT

DEBUG = False

with open('input.txt', 'r') as f:
    disk_map = f.read().strip()

# disk_map = "2333133121414131402"    # Example 1
# disk_map = "12345"                  # Example 2

data = [int(e) for e in disk_map[::2]]            # Data is on even indexes
empty_space = [int(e) for e in disk_map[1::2]]    # Empty space is on odd indexes

print(f'Data : {data}') if DEBUG else None
print(f'Empty space : {empty_space}') if DEBUG else None

# Part 1 (optimized)
total = 0

cursor = 0          # Current position on disk (block number)
file_id = 0         # Current position in the data or empty_space string
data_flag = True    # whether we are in data or empty_space
while len(disk_map):
    print("----------------------------------------------") if DEBUG else None
    if data_flag:
        # print "Reading data" in yellow
        print(f'\033[33mReading data\033[0m') if DEBUG else None

    else:
        # print "Filling empty space" in green
        print(f'\033[32mFilling empty space\033[0m') if DEBUG else None
    print(f'Current position in disk : {cursor}') if DEBUG else None
    print(f'Current file id : {file_id}') if DEBUG else None

    if data[-1] == 0: # If the last file is empty, it has been moved entirely to fill empty space
            data.pop()      # so we can remove it
    
    if all(e == 0 for e in data):
        print(f'All data is read') if DEBUG else None
        break

    # Read the current file
    if data_flag:
        # If we reached EOF, switch to empty_space
        if data[file_id] == 0:
            data_flag = False
            print(f'EOF, switching to empty space') if DEBUG else None
            continue

        # If we are not at the EOF, add i*file_id to the total
        total += cursor*file_id
        print(f'{cursor} * {file_id} = {cursor*file_id}') if DEBUG else None
        data[file_id] -= 1

    # Fill the empty space with data
    else:    
        # If we reached EOF, switch to data
        if empty_space[file_id] == 0:
            data_flag = True
            file_id += 1
            print(f'EOF, switching to data') if DEBUG else None
            continue

        # If we are not at the EOF, fill the empty space with the data from the last file
        total += cursor*(len(data)-1)
        print(f'{cursor} * {len(data)-1} = {cursor*(len(data)-1)}') if DEBUG else None
        data[-1] -= 1
        empty_space[file_id] -= 1

    print(f"Data : {data}") if DEBUG else None
    print(f"Empty space : {empty_space}") if DEBUG else None
    print(f'Total : {total}') if DEBUG else None
    cursor+=1

print(f'Part 1 : {total}')


# Part 2
total = 0


print(f'Part 2 : {total}')
