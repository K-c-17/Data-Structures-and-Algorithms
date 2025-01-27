'''
Implementation of Binary search algorithm in Python
'''

def binarySearch(array, target):

    #declaring two pointers
    left=0
    right=len(array) - 1

    #print(f'value of sorted array:{array}')
    

    while left<=right:
        
        #computing the middle value
        middle=(left+right)//2
        
        #print(f'Value of middle: {array[middle]}')
        if array[middle]==target:
            return middle
        
        elif array[middle] > target:
            right=middle - 1
        
        else:
            left=middle + 1
        #print(f'Value of right:{right}\n Value of left:{left}\n')
    
    #if the element is not found
    return -1



result=binarySearch([1,32,345,233,546,3454,34,34,65,1,3,4],345)

print(result)


'''
Time Complexity: O(logN)
Space Complexity: O(1)
'''

