# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:03:57 2022

@author: Ксения
"""

# Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала для каждого предприятия. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше
# среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


from collections import namedtuple
from statistics import mean

company = namedtuple('company', 'name profit_list avg')

new_list = []
for i in range(int(input('Введите количество компаний: '))):
    arg = input('Введите название компании и прибыль через пробел:\n').split()
    new_list.append(company(arg[0], arg[1:], mean(map(int, arg[1:3]))))

avg = mean([i.avg for i in new_list])

for i in new_list:
    print(f'Компания: {i.name} \t\tСредняя прибыль за год: {i.avg}')

print('Компании с прибылью ниже среднего:')
for i in new_list:
    if i.avg < avg:
        print(i.name)

print('Компании с прибылью выше среднего:')
for i in new_list:
    if i.avg > avg:
        print(i.name)
        