# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:49:31 2022

@author: Ксения Камнева
"""

while True:
    num = input('Введите натуральное число: ')
    i = len(num) - 1
    try:        
        num = int(num)
    except ValueError:
        print('Неверный формат данных!')
        continue
    if num > 0:
        break
    print('Вы ввели отрицательное число или нуль.')
    
rev_num = 0
old_num = num
while num > 0:
    rev_num += (num % 10) * 10 ** i
    num = num // 10
    i -= 1
print(f'{rev_num} обратное числу {old_num}.')
