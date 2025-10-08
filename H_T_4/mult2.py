import random

def vec_times_matr(l, m, n):
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