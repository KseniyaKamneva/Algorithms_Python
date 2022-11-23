# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 01:23:34 2022

@author: Ксения
"""

# Задача 4: Пользователь вводит две буквы. Определить на каких местах
# алфавита они стоят и сколько между ними находится букв.

first_letter = input('Введите первую строчную букву латинского алфавита: ')
second_letter = input('Введите вторую строчную букву латинского алфавита: ')

if first_letter.isalpha() and second_letter.isalpha():
    if first_letter.islower() and second_letter.islower():
        if len(first_letter) == 1 and len(second_letter) == 1:
            if 96 < ord(first_letter) < 123 and 96 < ord(second_letter) < 123:
                first_num = ord(first_letter) - ord('a') + 1
                second_num = ord(second_letter) - ord('a') + 1
                dist_num = abs(first_num - second_num) - 1
                print(f'{first_letter} стоит на {first_num} месте.')
                print(f'Буква {second_letter} стоит на {second_num} месте.')
                print(f'Между ними {dist_num} букв.')
            else:
                print('Это не латинские строчные буквы!')
        else:
            print('Введено больше одной буквы!')
    else:
        print('Это прописные буквы!')
else:
    print('Неверный формат данных!')
