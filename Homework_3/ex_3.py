# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:03:58 2022

@author: Ксения Камнева
"""
from random import randint

min_elem = 100
min_i = 0
max_elem = -101
max_i = 0
i = 0

ran_array = [randint(-100,100) for _ in range(10)]
print(f'Исходный список:\n{ran_array}')

while i < 10:
    if ran_array[i] < min_elem:
        min_elem = ran_array[i]
        min_i = i
    if ran_array[i] > max_elem:
        max_elem = ran_array[i]
        max_i = i
    i += 1
    
ran_array[min_i] = max_elem
ran_array[max_i] = min_elem
print(f'Результат:\n{ran_array}')
