disk = "00992111777.44.333....5555.6666.....8888.."
total = 0
for i in range(len(disk)):
    if disk[i] == '.':
        print(f'Skip {i}')
        continue
    total += i*int(disk[i])
    print(f'{i} * {disk[i]} = {i*int(disk[i])} (total = {total})')