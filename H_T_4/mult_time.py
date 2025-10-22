import random

def matr_times_matr(a, b, c, d):
    matr_1 = []
    for i in range(a):
        matr_1_row = []
        for j in range(b):
            matr_1_row.append(random.randint(0, 10))
        matr_1.append(matr_1_row)

    matr_2 = []
    for i in range(c):
        matr_2_row = []
        for j in range(d):
            matr_2_row.append(random.randint(0, 10))
        matr_2.append(matr_2_row)

    mult = []
    for i in range(a):
        mult_row = []
        for k in range(d):
            summ = 0
            for f in range(c):
                summ += matr_1[i][f] * matr_2[f][k]
            mult_row.append(summ)
        mult.append(mult_row)