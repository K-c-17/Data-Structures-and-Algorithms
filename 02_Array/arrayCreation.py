'''
Creating array
'''

#using the array module
import array

my_array=array.array("i")
print(my_array)

my_array1=array.array("i",[1,2,3,4,5])
print(my_array1)


#using the numpy module
import numpy as np          #Module provides a feature rich and high preformance array object

np_array=np.array([],dtype=int)    #just creates np_array object in memory but doesn't allocate any memory since the array is empty
print(np_array) 

np_array1=np.array([1,2,3,4,5])    #creates np_array object and also allocated it a set of contiguous blocks in memory
print(np_array1)


'''
Creating an array object from both Array module as well as Numpy module has O(1) complexity
Since creating an empty array involves minimal operations such as intializing the array metadata
and allocating a minimal amount of memory of array elements
Space complexity = O(1)         [Since an empty array occupies minimum to no memory]


For creating a non-empty array:
Time Complexity= O(N)       (Since it basically involves copying the elements from an iterable into the array)
Space Complexity= O(N)      (Memory allocation depends on the number of elements)

'''
