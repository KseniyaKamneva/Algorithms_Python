# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 23:33:00 2022

@author: Ксения Камнева
"""

while True:
    try:
        num = int(input('Введите натуральное число: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if num > 0:
        break
    print('Вы ввели отрицательное число или нуль.')

even_num = 0
odd_num = 0
old_num = num
while num > 0:
    if num % 2 == 0 :
        even_num += 1
    else:
        odd_num += 1
    num = num // 10
print(f'В числе {old_num} чётных цифр: {even_num}, нечётных цифр: {odd_num}.')
   