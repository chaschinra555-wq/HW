import random

matr = []
def sum_trace_elements(a):
    t = 0
    suma = 0
    for i in range(a):
        matr_row = []
        for j in range(a):
            matr_row.append(random.randint(0, 10))
            if t == j:
                suma += matr_row[j]
        t += 1
        matr.append(matr_row)
    print(matr)
    return suma