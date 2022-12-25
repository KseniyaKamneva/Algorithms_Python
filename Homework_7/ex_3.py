# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 12:16:18 2022

@author: Ксения
"""

import random

m = int(input('Введите m: '))
array = [random.randint(-100, 100) for _ in range(2 * m + 1)]


def median(nums):
    med = len(nums) // 2
    nums.sort()
    if not len(nums) % 2:
        return (nums[med - 1] + nums[med]) / 2
    return nums[med]


print('Исходный массив:', array)
print('Медиана:', median(array[:]))
