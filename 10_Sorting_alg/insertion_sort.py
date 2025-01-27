'''
Implementation of Insertion Sort
Language: Python

'''

def insertionSort(customList):
    for i in range(1,len(customList)):
        curr=customList[i]
        j=i-1
        while j>=0 and curr<customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=curr
    print(customList)


lst=[22,12,34,23]
insertionSort(lst)


'''
Time Complexity: O(N^2)
Space Complexity: O(1) {since the sorting is in-place}
'''



