# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:41:20 2022

@author: Ксения Камнева
"""

num = 2
multiple_of_2 = 0
multiple_of_3 = 0
multiple_of_4 = 0
multiple_of_5 = 0
multiple_of_6 = 0
multiple_of_7 = 0
multiple_of_8 = 0
multiple_of_9 = 0

while num < 100:
    if num % 2 == 0:
        multiple_of_2 += 1
    if num % 3 == 0:
        multiple_of_3 += 1
    if num % 4 == 0:
        multiple_of_4 += 1
    if num % 5 == 0:
        multiple_of_5 += 1
    if num % 6 == 0:
        multiple_of_6 += 1
    if num % 7 == 0:
        multiple_of_7 += 1
    if num % 8 == 0:
        multiple_of_8 += 1
    if num % 9 == 0:
        multiple_of_9 += 1
    num += 1

print(f'В диапазоне от 2 до 99 чисел кратных 2 - {multiple_of_2},')
print(f'кратных 3 - {multiple_of_3}, кратных 4 - {multiple_of_4},')
print(f'кратных 5 - {multiple_of_5}, кратных 6 - {multiple_of_6},') 
print(f'кратных 7 - {multiple_of_7}, кратных 8 - {multiple_of_8},')  
print(f'кратных 9 - {multiple_of_9}.')
     