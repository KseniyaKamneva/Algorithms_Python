# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 00:00:42 2022

@author: Ксения Камнева
"""

while True:
    try:        
        num = int(input('Введите количество элементов: '))
    except ValueError:
        print('Неверный формат данных!')
        continue
    if num > 0:
        break
    print('Вы ввели отрицательное число или нуль.')

i = 0
sum_num = 0
row = ''
while num > i:
    if i == 0:
        row += str(1 / (-2) ** i)
    else:
        row += ', ' + str(1 / (-2) ** i)
    sum_num += 1 / (-2) ** i
    i += 1
print(f'Сумма ряда [{row}] равна {sum_num}.')
