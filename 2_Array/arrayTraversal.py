import array
import numpy as np


'''
Array Traversal
'''

arr1=array.array('i',[1,2,3,4,5,6])
arr2=array.array('d',[1.1,1.3,2.1])

def traverse_arr(arr):
    for i in arr:
        print(i)

traverse_arr(arr1)

'''
Traversing the array:
Time complexity = O(N)              since we have to traverse the entire array
Space complexity = O(1)             since we don't need an extra location to perform this operation
'''