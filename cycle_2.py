a = 1
for row in range(1, 6):
    line = ''
    for col in range(1, 6):
            if (row + col) % 2 != 0:
                line += f'{a}\t'
                a += 1
            else:
                line += '*\t'
    print(line)