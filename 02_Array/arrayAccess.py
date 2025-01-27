import array
import numpy as np

'''
Accessing the element of an array
'''
#general syntax is <array>[index]


arr1=array.array('i',[1,2,3,4,5,6])

def accessElement(arr,index):
    if index>=len(arr):
        print("Index out of bounds error")
    else:
        print(arr[index])

accessElement(arr1,1)

'''
Complexity of Accessing the element of an array
Time complexity: O(1)               
Space complexity: O(1)                  since we don't need extra space here to perform this operation
'''