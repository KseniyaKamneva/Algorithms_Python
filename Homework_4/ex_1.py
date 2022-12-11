# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:07:13 2022

@author: Ксения
"""
import sys
from functools import reduce

import big_o


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

    return result


def count_with_sum(arr: list):
    min_elem, *_, max_elem = sorted(arr)
    min_i, max_i = arr.index(min_elem), arr.index(max_elem)

    if min_i > max_i:
        min_i, max_i = max_i, min_i

    elems = arr[min_i + 1 : max_i]
    return sum(elems)


def count_with_reduce(arr: list):
    min_elem, *_, max_elem = sorted(arr)
    min_i, max_i = arr.index(min_elem), arr.index(max_elem)

    if min_i > max_i:
        min_i, max_i = max_i, min_i

    elems = arr[min_i + 1 : max_i]
    return reduce(lambda x, y: x + y, elems, 0)


def sum_array_elems_between_min_and_max(arr):
    print("Массив:", arr)
    print()
    data_generator = lambda _: arr
    results = {}

    for func in (compare, count_with_sum, count_with_reduce):
        best, _ = big_o.big_o(func, data_generator, n_repeats=100)
        results[func.__name__] = best.coeff

        complexity, time = str(best).split(":", maxsplit=1)
        raw_time, _ = time.split(" = ")[1].split(" (")

        print("Алгоритм:", func.__name__)
        print("Время исполнения:", raw_time, "сек.")
        print("Сложность:", complexity)
        print()

    fastest_algo = min(results.values())
    for algo_name, algo_res in results.items():
        if algo_res is fastest_algo:
            print(f"Наиболее быстрый алгоритм – {algo_name}")
            break


if __name__ == "__main__":
    n: str = sys.argv[-1]

    if n.isdecimal():
        n = int(n)
    else:
        n = 10

    print("Количество элементов в массиве:", n)

    arr = big_o.datagen.integers(n, -100, 100)
    sum_array_elems_between_min_and_max(arr)
