# -*- coding: utf-8 -*-
"""
Created on Mon May 13 15:59:06 2024

@author: connie
"""

def sorting_function(array):
    if len(array) <= 1:
        return array
    middle = array[len(array) // 2]
    left, right = [], []
    for item in array:
        if item < middle:
            left.append(item)       
        elif item > middle:
            right.append(item)
            
    left = sorting_function(left)
    right = sorting_function(right)
    
    print(f'現在用 {middle} 排序陣列 {array}: ')
    print(f'左陣列: {left}')
    print(f'右陣列: {right}')
    print('排序過的陣列:')
    return left + [middle] + right

print(sorting_function([33, 67, 8, 13, 54, 119, 3, 84, 25, 41]))