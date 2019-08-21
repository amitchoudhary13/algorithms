# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 17:00:45 2019

@author: amit
"""

def interpolationSearch(arr,n,x):
    start = 0
    end = (n-1)
    
    while start <= end and x >= arr[start] and x <= arr[end]:
        if start == end:
            if arr[start] == x:
                return start;
            return -1;
        pos = start + int(((float(end - start)/(arr[end]-arr[start]))*(x -arr[start])))
        if arr[pos] == x:
            return pos;
        if arr[pos] < x :
            start = pos + 1;
        else:
            end = pos -1 ;
    
    return -1;
    
    
# Array of items oin which search will be conducted 
arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47] 
n = len(arr) 
  
x = 18 # Element to be searched 
index = interpolationSearch(arr, n, x) 
index =1  
if index != -1: 
    print( "Element found at index",index )
else: 
    print( "Element not found")
