import random

def vec_times_vec(a):
    scal_mult = 0
    vec_1 = []
    for i in range(a):
        vec_1.append(random.randint(0, 10))
    print(vec_1)

    vec_2 = []
    for i in range(a):
        vec_2.append(random.randint(0, 10))
        scal_mult += vec_1[i] * vec_2[i]
    print(vec_2)

    return scal_mult