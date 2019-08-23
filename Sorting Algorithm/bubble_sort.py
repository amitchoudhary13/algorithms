# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:22:01 2019

@author: amit
"""
def bubble_sort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
  
bubble_sort(arr) 
  
