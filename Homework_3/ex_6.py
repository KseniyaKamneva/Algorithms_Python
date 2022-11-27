# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:11:13 2022

@author: Ксения Камнева
"""
from random import randint

min_elem = 100
min_i = 0
max_elem = -101
max_i = 0
i = 0
sum_arr = 0

ran_array = [randint(-100,100) for _ in range(10)]

while i < 10:
    if ran_array[i] < min_elem:
        min_elem = ran_array[i]
        min_i = i
    if ran_array[i] > max_elem:
        max_elem = ran_array[i]
        max_i = i
    i += 1

if min_i < max_i:
    i = min_i + 1
    while i < max_i:
        sum_arr += ran_array[i]
        i += 1
if min_i > max_i:
    i = max_i + 1
    while i < min_i:
        sum_arr += ran_array[i]
        i += 1
        
print(f'Массив:\n{ran_array}')
print(f'Сумма чисел между минимальным и максимальным элементами равна {sum_arr}')
