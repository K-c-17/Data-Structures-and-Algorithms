import array 
import numpy as np

'''
Elements insertion in an array
'''


#inserting elements in the beginning of an array
my_array1=array.array('i',[1,2,3,4,5])
print(my_array1)
my_array1.insert(0,6)
print(my_array1)

'''
Complexities of array insertion (inserting in the starting of array (worst case)):
Time complexity = O(n)
Space Complexity = O(1)
'''