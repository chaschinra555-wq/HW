import math

n = int(input('размерность таблицы умножения: '))

for k in range(1, math.ceil(n / 5) + 1): 
    for i in range (1, n + 1):
            line = ''
            for j in range (5*k - 4, 5*k - 4 + 5):
                    line += f'{j} * {i} = {i*j}\t'
                    if j == n: break
            print(line)
            
    print()