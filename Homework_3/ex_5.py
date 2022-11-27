# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:00:29 2022

@author: Ксения Камнева
"""

from random import randint

i = 0
res_i = 0
res = -101
ran_array = [randint(-100,100) for _ in range(10)]

while i < 10:
    if ran_array[i] < 0 and ran_array[i] > res:
        res = ran_array[i]
        res_i = i + 1
    i += 1

print(f'Массив:\n{ran_array}')
print(f'Максимальный отрицательный элемент массива стоит на {res_i} позиции и равен {res}')
