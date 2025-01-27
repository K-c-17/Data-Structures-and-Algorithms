import array
import numpy as np


'''
Searching the element in an array
'''

arr1=array.array('i',[1,2,3,4,5,6])

def linear_search(arr,target):
    for i in range(0,len(arr)):
        if arr[i]==target:
            return i
    return -1 

print(linear_search(arr1,1))

'''
Complexity of searching an element in an array:
Time complexity = O(n)
Space complexity = O(1)             you don't need to store anything specific for this operation

Range function has a time complexity of O(1) and space complexity of O(1) as well since it doesn't actually
generate a sequence of number it basically provides numbers on demand for each loop
'''