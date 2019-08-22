# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:04:28 2019
@author: Amit
"""
def binarySearch(arr, l, r, x):
    while r >= l:
        mid = int(l + (r - l)/2)
        if arr[mid] == x :
            return mid;
        elif arr[mid] > x:
            return binarySearch(arr,l,mid-1,x)
        elif arr[mid] < x:
            return binarySearch(arr,mid+1,r,x)
     else: 
        # Element is not present in the array 
        return -1



arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index %d" % result )
else: 
    print("Element is not present in array")
