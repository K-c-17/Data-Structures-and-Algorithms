'''
Implementation of Linear Search in Python
'''

def linearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1


#calling the linear search function
result=linearSearch([20,40,30,50,90], 100)

#printing the final result
print(result)



'''
Time Complexity: O(N)
Space Complexity: O(1)
'''
