import array
 
my_array=array.array("i")
print(my_array)

my_array1=array.array("i",[1,2,3,4,5])
print(my_array1)


import numpy as np
np_array=np.array([],dtype=int) #way to initialize a blank array
print(np_array)

np_array2=np.array([1,2,3,4,5]) #no need to provide a data type
print(np_array2)


#insertion to array

my_array1.insert(5,6)
print(my_array1)

#traversing an array
ar1=array.array("i",[1,2,3,45,334,345,23,234,546,46534,3534,345,34534])

def arr_traversal(arr):
    for i in arr:
        print(i)

arr_traversal(ar1)

#acessing an element in an array
def accessElement(ar,ind):
    if ind >= len(ar):
        print("There is no element with this index in this array")
    else:
        print(ar[ind])
accessElement(ar1,6)

#searching an element in an array
'''
def linearSearch(arr,value):
    for i in arr:
        if i==value:
            return print("Value found in the input array \n" )
    return print("value not found in the input array")

linearSearch(ar1,334)
'''

def linearSearch(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return print(str(arr[i])+ " is present in the input array on index: "+ str(i))
    return -1

linearSearch(ar1,3)

#deletion from an array
ar1.remove(3)
print(ar1)

                  
