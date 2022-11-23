# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 22:22:58 2022

@author: Ксения Камнева
"""


def calculate(sign):
    if sign not in '+-*/':
        print('Такой операции нет.')
        return False
    elif sign == '+':
        print(f'{a} + {b} = ', a + b)
    elif sign == '-':
        print(f'{a} - {b} = ', a - b)
    elif sign == '*':
        print(f'{a} * {b} = ', a * b)
    elif sign == '/':
        if b != 0: 
            print(f'{a} / {b} = ', a / b)
        else:
            print('Делить на нуль нельзя.')
    return True

        
repeat = True
while repeat:
    try:
        a = int(input('Введите первое число: '))
        b = int(input('Введите второе число: '))
        while True:
            sign = input('Введите операцию +, -, *, /, либо 0 для выхода: ')
            if sign == '0':
                print('Выход.')
                repeat = False
                break
            calc = calculate(sign)
            if calc is True:
                break
    except ValueError:
        print('Неверный формат данных!')  
 