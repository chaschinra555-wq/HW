'''function - 1'''

print('Для вывода таблицы сложения введите "1"')
print('Для вывода таблицы вычитания введите "2"')
print('Для вывода таблицы умножения введите "3"')
print('Для вывода таблицы деления введите "4"')
operation = int(input('Введите цифру от 1 до 4: '))

def func(operation):
    if operation == 3:
        print('-----Таблица умножения-----')
        for k in range(1, 3):
            for i in range(1, 10):
                for j in range(5*k - 4, 5*k - 4 + 5):
                    print (f'{i} * {j} = {(i * j)}\t', end = ' ')
                print()
            print()

    if operation == 4:
        print('-----Таблица деления-----')
        for k in range(1, 3):
            for i in range(1, 10):
                for j in range(5*k - 4, 5*k - 4 + 5):
                    print(f'{i * j} / {j} = {i}\t', end = ' ')
                print()
            print()

    if operation == 1:
        print('-----Таблица сложения-----')
        for k in range(1, 3):
            for i in range(1, 10):
                for j in range(5*k - 4, 5*k - 4 + 5):
                    print(f'{i} + {j} = {i + j}\t', end = ' ')
                print()
            print()

    if operation == 2:
        print('-----Таблица вычитания-----')
        for k in range(1, 3):
            for i in range(1, 10):
                for j in range(5*k - 4, 5*k - 4 + 5):
                    if (i - j) <= 0:
                        print(f'{j} - {i} = {j - i}\t', end = ' ')
                    else:
                        print(f'{i} - {j} = {i - j}\t', end = ' ')
                print()
            print()

func(operation)



'''function - 2'''
print('-----Создание вектора длины n-----')

import random

n = int(input('Длина вектора: '))

def vector(n):
    list = []
    for i in range(n):
        list.append(round(random.uniform(0, 1), 3))
    return list
    
vector(n)



print('-----Создание матрицы m*n-----')

import random

m = int(input('Число строк матрицы: '))
n = int(input('Число столбцов матрицы: '))

def matrix(m, n):
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            b.append(round(random.uniform(0, 1), 3))
        a.append(b)
    return(a)

matrix(m, n)



print('-----Произведение вектора на матрицу-----')

import random

l = int(input('Размер вектора l: '))
m = int(input('Число строк матрицы m: '))
n = int(input('Число столбцов матрицы n: '))

print(f'-----Матрица {m}x{n}-----')
def prod(l, m, n):
    if l == n:
        c = []
        for i in range(l):
            c.append(random.randint(0, 100))
            
        a = []
        mult1 = []
        for i in range(m):
            b = []
            summ = 0
            for j in range(n):
                b.append(random.randint(0, 100))
                summ += b[j] * c[j]
            mult1.append(summ)
            print(b)    
            a.append(b)
        print(f'-----Вектор 1x{l}-----')
        print(c)
        print(f'-----Произведение матрицы на вектор-----')
        print(mult1)
    else:
        print('Умножение невозможно!')

prod(l, m, n)



print('-----Создание и печать вектора длины n-----')

import random

n = int(input('Длина вектора: '))

def vector(n):
    list = []
    for i in range(n):
        list.append(round(random.uniform(0, 1), 3))
    print(list)
    
vector(n)



print('-----Создание и печать матрицы m*n-----')

import random

m = int(input('Число строк матрицы: '))
n = int(input('Число столбцов матрицы: '))

def matrix(m, n):
    a = []
    for i in range(m):
        b = []
        for j in range(n):
            b.append(round(random.uniform(0, 1), 3))
        a.append(b)
        print(a[i])

matrix(m, n)



print('-----Сумма элементов диагонали матрицы-----')

import random

n = int(input('Размер матрицы n на n: '))

column = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(random.randint(0, 100))
    print(row)
    column.append(row)
    
def sum_diag(n, a):
    suma = 0
    for i in range(n):
        suma += a[i][i]
    return suma
    
print(sum_diag(n, column))



print('-----Двумерная свертка изображения-----')

import random

def matrix(m, n):
    nested_list = []
    for i in range(m):
        inner_list = []

        for j in range(n):
            inner_list.append(random.randint(0, 10))
        nested_list.append(inner_list)

    return nested_list

def svertka(picture, kernel):
    picture_rows = len(picture)
    picture_columns = len(picture[0])
    
    kernel_rows = len(kernel)
    kernel_columns = len(kernel[0])
        
    output_rows = picture_rows - kernel_rows + 1
    output_columns = picture_columns - kernel_columns + 1
    
    output_matrix = [[0 for i in range(output_rows)] for j in range(output_columns)]
    
    for i in range(output_rows):
        for j in range(output_columns):
            suma = 0
            for x in range(kernel_rows):
                for y in range(kernel_columns):
                    add = picture[x + i][y + j] * kernel[x][y]
                    suma += add
            output_matrix[i][j] = suma
            
    return output_matrix
    
a = int(input('Введиет число строк в матрице-изображении: '))
b = int(input('Введиет число столбцов в матрице-изображении: '))
c = int(input('Введиет число строк в матрице-ядре: '))
d = int(input('Введиет число столбцов в матрице-ядре: '))

if c > a or d > b:
    print('Ядро не может быть больше изображения!!!')
else:
    pict = matrix(a, b)
    print('-----Матрица-изображение-----')
    print(pict)
    kern = matrix(c, d)
    print('-----Матрица-ядро-----')
    print(kern)
    print('-----Матрица-свертка-----')
    print(svertka(pict, kern))