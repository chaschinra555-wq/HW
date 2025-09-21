'''cycle - 1'''

while True:
        a = float(input("the first number: "))
        b = float(input("the second number: "))
        print(f'the sum of {a} and {b}: {a + b}')




'''cycle - 2'''

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




'''cycle - 3'''

import random

num = int(input('my figure: '))
a = int(input('the beginning of the interval: '))
b = int(input('the end of the interval: '))

c = num + 1
while c != num:
    c = random.randint(a, b)
    print(c)
    if (c == num):
        print(f'yes! \nmy figure is {num}! \ncongratulations!')




'''cycle - 4'''

a = -1
b = 0

while a != 0:
    a = int(input())
    if a > b:
        b = a

print(b)




'''cycle - 5'''

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




'''list - 1'''

import random

n = int(input('количество чисел в списке: '))
list = []

for i in range(n):
    list.append(random.randint(-10000, 10000))
    
print(list)

list.sort()

print(f'минимальное число в выборке: {min(list)}')
print(f'максимальное число в выборке: {max(list)}')
print(f'медиана в выборке: {list[(n - 1) // 2]}')




'''list - 2'''

import random

n = 20
list = []
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

for i in range(20):
    t = random.randint(0, 99)
    if 0 <= t <= 9:
        n1 += 1
    elif 10 <= t <= 19:
        n2 += 1
    elif 20 <= t <= 29:
        n3 += 1
    elif 30 <= t <= 39:
        n4 += 1
    elif 40 <= t <= 49:
        n5 += 1
    elif 50 <= t <= 59:
        n6 += 1
    elif 60 <= t <= 69:
        n7 += 1
    elif 70 <= t <= 79:
        n8 += 1
    elif 80 <= t <= 89:
        n9 += 1
    else:
        n10 += 1

list = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

for i in range (len(list)):
    print(f'{i + 1}) количество элементов из отрезка [{i}0; {i}9]: {list[i]}')
    print(f'вероятность встречаемости числа из отрезка [{i}0; {i}9]: {round(list[i]/n, 2)}\n')




'''list - 3'''

import random

n = int(input('размерность векторов: '))
a = int(input('скаляр: '))
k = 1

vec_1, vec_2 = [], []
summ, mult_vec_vec, mult_vec_scal = [], [], []
len_1, len_2 = 0, 0

for i in range(n):
    vec_1.append(random.randint(-100, 100))
    len_1 += vec_1[i] * vec_1[i]

for i in range(n):
    vec_2.append(random.randint(-100, 100))
    len_2 += vec_2[i] * vec_2[i]
    summ.append(vec_1[i] + vec_2[i])
    mult_vec_vec.append(vec_1[i] * vec_2[i])
    
if len_1 > len_2:
    mult_vec_scal = [vec * a for vec in vec_1]
else:
    mult_vec_scal = [vec * a for vec in vec_2]
    k = 2
    
print(f'первый веткор: {vec_1}')
print(f'второй веткор: {vec_2}')
print(f'покомпонентная сумма векторов: {summ}')
print(f'покомпонентное произведение векторов: {mult_vec_vec}')
print(f'умножение скаляра на вектор 1: {mult_vec_scal}' if k == 1 else f'умножение скаляра на вектор 2: {mult_vec_scal}')




'''list - 4'''

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec = [1, 2, 3]
summ = 0

b = []


for i in range(len(a)):
    for j in range(len(a[i])):
        summ += a[i][j] * vec[j]
    b.append(summ)
    summ = 0
    
print(f'исходная матрица:')
for i in range(len(a)):
    print(a[i][0], a[i][1], a[i][2])
print(f'исходный вектор: ')
for i in range(len(vec)):
    print(vec[i])
print(f'произведение матрицы на веткор: ')
for i in range(len(b)):
    print(b[i])
