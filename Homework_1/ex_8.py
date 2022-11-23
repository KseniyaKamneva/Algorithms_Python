# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 21:46:41 2022

@author: Ксения
"""
#Задача 8: Вводятся три разных числа. Найти, какое из них является средним 
#(больше одного, но меньше другого).

first_num = input('Введите первое число: ')
second_num = input('Введите второе число: ')
third_num = input('Введите третье число: ')
flag = False
try:
    first_num = float(first_num)
    second_num = float(second_num)
    third_num = float(third_num)
    flag = True
except ValueError:
        print('Неверный формат данных!')
        
if flag == True:
    first_max = max(first_num, second_num)
    second_max = max(second_num, third_num)
    print('Среднее число равно ', min(first_max, second_max))

#Если требуется узнать порядковый номер числа, то решение будет таким:
if flag == True:
    first_max = max(first_num, second_num)
    second_max = max(second_num, third_num)
    min_max = min(first_max, second_max)
    if second_num == min_max:
        print('Средним является второе число ', second_num)
    elif third_num == min_max:
        print('Средним является третье число ', third_num)
    else:
        print('Среднее первое число ', first_num)
