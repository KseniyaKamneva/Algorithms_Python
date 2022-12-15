# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 16:38:20 2022

@author: Ксения
"""

# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.

from collections import defaultdict
from collections import deque


def dexx(string):
    dex = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex += data[num[i]] * 16 ** i
    return dex


def hexx(numb):
    num = deque()
    while numb > 0:
        d = numb % 16
        for i in data:
            if data[i] == d:
                num.append(i)
        numb //= 16
    num.reverse()
    return list(num)


alphabet = '0123456789ABCDEF'
data = defaultdict(int)
counter = 0
for key in alphabet:
    data[key] += counter
    counter += 1

first_num = dexx(input('Введите первое шестнадцатиричное число:\n ').upper())
second_num = dexx(input('Введите второе шестнадцатиричное число:\n ').upper())

print(f'Сумма чисел: {hexx(first_num + second_num)}')
print(f'Произведение чисел: {hexx(first_num * second_num)}')
