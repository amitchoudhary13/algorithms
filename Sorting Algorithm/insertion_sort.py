# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:10:00 2019

@author: amit

"""



def insertion_sort(arr):
    for i in range(0,len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]> key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key






arr = [64, 34, 25, 12, 22, 11, 90] 
  
insertion_sort(arr) 
