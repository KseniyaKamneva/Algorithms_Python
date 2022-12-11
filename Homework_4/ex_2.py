# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:17:27 2022

@author: Ксения
"""
from math import sqrt

import big_o


def sieve(n):
    length = 10000
    lst = [i for i in range(length)]
    lst[1] = 0
    for i in range(2, length):
        if lst[i] != 0:
            j = i * 2
            while j < length:
                lst[j] = 0
                j += i
    result = [i for i in lst if i != 0]
    return result[n - 1]


def prime(n):
    length = 10000
    lst = [i for i in range(length)]
    lst[1] = 0
    ev_num = lst[2]
    for num in range(2, length):
        primary = True
        while ev_num <= sqrt(lst[num]) and primary is True:
            if lst[num] % ev_num == 0:
                primary = False
                ev_num += 1
            if not primary:
                lst[num] = 0
    result = [i for i in lst if i != 0]
    return result[n - 1]


def find_primes():
    data_generator = lambda _: 10
    results = {}

    for func in (sieve, prime):
        best, _ = big_o.big_o(func, data_generator, min_n=1, max_n=100, n_repeats=10)
        results[func.__name__] = best

        complexity, time = str(best).split(":", maxsplit=1)
        raw_time, _ = time.split(" = ")[1].split(" (")

        print("Алгоритм:", func.__name__)
        print("Время исполнения:", raw_time, "сек.")
        print("Сложность:", complexity)
        print()

    fastest_algo = min(results.values())
    print(fastest_algo)
    for algo_name, algo_res in results.items():
        if algo_res is fastest_algo:
            print(f"Наиболее быстрый алгоритм – {algo_name}")
            break


if __name__ == "__main__":
    find_primes()
