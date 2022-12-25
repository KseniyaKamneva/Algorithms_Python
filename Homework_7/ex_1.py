# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:17:13 2022

@author: Ксения
"""
import random

array = [random.randint(-100, 100) for _ in range(10)]


def bubble_sort(nums):
    for j in range(len(nums) - 1):
        for i in range(len(nums) - 1 - j):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


print('Исходный массив:', array)
print('Пузырьковая сортировка:', bubble_sort(array[:]))
