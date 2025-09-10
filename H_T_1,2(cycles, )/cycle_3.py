import random

num = int(input('my figure: '))
a = int(input('the beginning of the interval: '))
b = int(input('the end of the interval: '))

c = int(num + 1)
while c != num:
    c = random.randint(a, b)
    print(c)
    if (c == num):
        print(f'yes! \nmy figure is {num}! \ncongratulations!')