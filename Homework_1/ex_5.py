# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:46:34 2022

@author: Ксения
"""
# Задача 5: Пользователь вводит номер буквы в алфавите. Определить, какая это 
# буква.

letter_num = input('Введите номер строчной буквы латинского алфавита: ')
flag = False
try:
    letter_num = int(letter_num)
    flag = True
except ValueError:
    print('Неверный формат данных!')

if flag == True:
    if 0 < letter_num < 27:
        letter_num += ord('a') - 1
        letter = chr(letter_num)
        print('Ваша буква:', letter)
    else:
        print('В латинском алфавите 26 букв.')
