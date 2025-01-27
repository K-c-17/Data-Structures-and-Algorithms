'''
Implementation of Selection Sort

'''

def selectionSort(customList):
    for i in range(len(customList)-1):
        min_ele_index = i
        for j in range(i+1,len(customList)):
            if customList[j]<customList[min_ele_index]:
                min_ele_index=j
        customList[i],customList[min_ele_index]=customList[min_ele_index],customList[i]
    
    print(customList)


lst=[22,12,34,23]

selectionSort(lst)

'''
For a selection sort:
Time Complexity= O(N^2)
Space Complexity= O(1)
'''
                


