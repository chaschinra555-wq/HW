'''
print('-----Задание 1.1 Произведение матрицы на матрицу с помощью модуля-----')

import mult1

a = int(input('Число строк первой матрицы a: '))
b = int(input('Число столбцов первой матрицы b: '))
c = int(input('Число строк второй матрицы c: '))
d = int(input('Число столбцов второй матрицы d: '))

mult1.matr_times_matr(a, b, c, d)
'''



'''
print('-----Задание 1.2 Произведение матрицы на вектор с помощью модуля-----')

import mult2

l = int(input('Размер вектора l: '))
m = int(input('Число строк матрицы m: '))
n = int(input('Число столбцов матрицы n: '))

mult2.vec_times_matr(l, m, n)
'''



'''
print('-----Задание 1.3 След матрицы-----')

import trace_matr

n = int(input('Размер квадратной матрицы n: '))

print(trace_matr.sum_trace_elements(n))
'''



'''
print('-----Задание 1.4 Скалярное произведение векторов-----')

import mult3

n = int(input('Размер вектора n: '))

print(mult3.vec_times_vec(n))
'''



'''
print('-----Задание 1.7.1 Запись данных в файл-----')

import file_write

file_write
'''


'''
print('-----Задание 1.7.2 Чтение данных из файла-----')

import file_read

file_read
'''



'''
print('-----Задание 2 Время перемножения матриц различного размера-----')

import mult_time, time

file = open('work_time.txt', 'w')

start_time_1 = time.perf_counter()
mult_time.matr_times_matr(10, 10, 10, 10)
end_time_1 = time.perf_counter()
print(f'Время перемножения двух матриц 10х10: {end_time_1 - start_time_1}')

start_time_2 = time.perf_counter()
mult_time.matr_times_matr(100, 100, 100, 100)
end_time_2 = time.perf_counter()
print(f'Время перемножения двух матриц 100х100: {end_time_2 - start_time_2}')

start_time_3 = time.perf_counter()
mult_time.matr_times_matr(1000, 1000, 1000, 1000)
end_time_3 = time.perf_counter()
print(f'Время перемножения двух матриц 1000х1000: {end_time_3 - start_time_3}')

file.write('Multiplication time of two 10x10 matrices: ' + str(end_time_1 - start_time_1) + 's' + '\n')
file.write('Multiplication time of two 100x100 matrices: ' + str(end_time_2 - start_time_2) + 's' + '\n')
file.write('Multiplication time of two 1000x1000 matrices: ' + str(end_time_3 - start_time_3) + 's' + '\n')

file.close()
'''

'''
def histogram_equalization(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    new_image = cv.equalizeHist(image)

    cv.imshow('Original Image', image)
    cv.imshow('New Image', new_image)
    cv.waitKey()


def contrast_changing(image):
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 1.0 # Simple contrast control
    beta = 0    # Simple brightness control
    # Initialize values
    print(' Basic Linear Transforms ')
    print('-------------------------')
    try:
        alpha = float(input('* Enter the alpha value [1.0-3.0]: '))
        beta = int(input('* Enter the beta value [0-100]: '))
    except ValueError:
        print('Error, not a number')
    # Do the operation new_image(i,j) = alpha*image(i,j) + beta
    # Instead of these 'for' loops we could have used simply:
    # new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    # but we wanted to show you how to access the pixels :)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
    cv.imshow('Original Image', image)
    cv.imshow('New Image', new_image)
    # Wait until user press some key
    cv.waitKey()


from builtins import input
import cv2 as cv
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Code for Changing the contrast and brightness of an image! tutorial.')
parser.add_argument('--input', help='Path to input image.', default='building.jpg')
args = parser.parse_args()

image = cv.imread(cv.samples.findFile(args.input))
if image is None:
    print('Could not open or find the image: ', args.input)
    exit(0)

action = int(input('Print 1 (Histogram Equalization) or 2 (Changing the contrast and brightness of an image!): '))
if action == 1:
    histogram_equalization(image)
elif action == 2:
    contrast_changing(image)
else:
    print('Error!')

'''
