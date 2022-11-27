# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 17:14:15 2022

@author: Ксения Камнева
"""

from random import randint

i = 0
res = []
ran_array = [randint(-100,100) for _ in range(10)]

while i < 10:
    if ran_array[i] % 2 == 0:
        res.append(i)
    i += 1

print(f'Массив:\n{ran_array}')
print(f'Массив индексов четных элементов:\n{res}')
