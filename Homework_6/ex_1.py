# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:07:13 2022

@author: Ксения
"""
import sys
from functools import reduce


def determine_size(elem, level=0):
    size_param = sys.getsizeof(elem)
    print('\t' * level, f'type={type(elem)}, size={size_param}, object={elem}')
    if hasattr(elem, '__iter__'):
        if hasattr(elem, 'items'):
            for key, value in elem.items():
                determine_size(key, level + 1)
                size_param = size_param + sys.getsizeof(key)
                determine_size(value, level + 1)
                size_param = size_param + sys.getsizeof(value)
        elif not isinstance(elem, str):
            for item in elem:
                determine_size(item, level + 1)
                size_param = size_param + sys.getsizeof(item)
    return size_param


def compare(arr):
    # Homework_3/ex_6.py
    min_elem, max_elem = 100, -101
    cur_i, min_i, max_i = 0, 0, 0
    result = 0
    n = len(arr)

    while cur_i < n:
        if arr[cur_i] < min_elem:
            min_elem = arr[cur_i]
            min_i = cur_i
        if arr[cur_i] > max_elem:
            max_elem = arr[cur_i]
            max_i = cur_i
        cur_i += 1

    if min_i < max_i:
        cur_i = min_i + 1
        while cur_i < max_i:
            result += arr[cur_i]
            cur_i += 1
    if min_i > max_i:
        cur_i = max_i + 1
        while cur_i < min_i:
            result += arr[cur_i]
            cur_i += 1
    print(f'Затрачено памяти: {determine_size(min_elem) + determine_size(max_elem) + determine_size(cur_i) + determine_size(min_i) + determine_size(max_i) + determine_size(result) + determine_size(n)}')
    return result


def count_with_sum(arr: list):
    min_elem, *_, max_elem = sorted(arr)
    min_i, max_i = arr.index(min_elem), arr.index(max_elem)

    if min_i > max_i:
        min_i, max_i = max_i, min_i

    elems = arr[min_i + 1 : max_i]
    print(f'Затрачено памяти: {determine_size(min_elem) + determine_size(max_elem)}')
    return sum(elems)


def count_with_reduce(arr: list):
    min_elem, *_, max_elem = sorted(arr)
    min_i, max_i = arr.index(min_elem), arr.index(max_elem)

    if min_i > max_i:
        min_i, max_i = max_i, min_i

    elems = arr[min_i + 1 : max_i]
    print(f'Затрачено памяти: {determine_size(min_elem) + determine_size(max_elem) + determine_size(min_i) + determine_size(max_i)}')
    return reduce(lambda x, y: x + y, elems, 0)


arr = [10, 5, 4, 8, 9, 20, 7, 6]
compare(arr)
count_with_sum(arr)
count_with_reduce(arr)

# По расходу памяти значительно выигрывает второй алгоритм, так как им затрачено в 
# два раза меньше памяти, чем в третьем, и почти в четыре раза меньше, чем в первом. 
