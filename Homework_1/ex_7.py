# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:18:33 2022

@author: Ксения
"""
# Задача 7: Определить, является ли год, который ввел пользователь, високосным
# или невисокосным.

year = input('Введите год: ')
flag = False
try:
    year = int(year)
    flag = True
except ValueError:
    print('Неверный формат данных!')

if flag == True:
    if year > 0:       
        modulo_400 = year % 400
        modulo_100 = year % 100
        modulo_4 = year % 4
        if modulo_400 == 0 or (modulo_4 == 0 and modulo_100 != 0):
            print('Это високосный год.')
        else:
            print('Это невисокосный год.')
    else:
        print('Программа рассчитывает ответ только для нашей эры.')
