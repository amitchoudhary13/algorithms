# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:01:25 2019

@author: Amit
"""

A = [34, 12, 63, 11, 5, 23] 

for i in range(len(A)):
    min_element = i
    for j in range(i+1,len(A)):
        if A[min_element] > A[j]:
            min_element = j
            
    temp = A [i]
    A[i] = A[min_element]
    A[min_element] = temp
