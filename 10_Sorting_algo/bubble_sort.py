'''
Implementation of Bubble Sort

'''

def bubbleSort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            print(i,j)
            if customList[j]> customList[j+1]:
                customList[j],customList[j+1]=customList[j+1],customList[j]
    print(customList)



lst=[1,2,34,45,45645,44,5,6,8,3,25,6,5,7454,34]

bubbleSort(lst)