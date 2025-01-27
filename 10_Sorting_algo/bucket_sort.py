'''
Implementation of Bucket sort.
Buckets are sorted using insertion sort

'''
import math

def insertionSort(customList):
    for i in range(1,len(customList)):
        curr=customList[i]
        j=i-1
        while j>=0 and curr<customList[j]:
            customList[j+1]=customList[j]
            j-=1
        customList[j+1]=curr
    return customList


def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))

    #initialzing the hashmap to collect the values of the buckets
    collector={}

    max_value=max(customList)
    
    #distribution in the buckets
    for i in customList:
        bucket=math.ceil(i * numberofBuckets / max_value)
        if bucket not in collector:
            collector[bucket]=[]
        else:
            collector[bucket].append(i)
    
    #sorting the individual buckets
    sorted_collector={key:insertionSort(value) for key,value in collector.items()}
    final_iter=[]
    
    #merging all the buckets
    for i in sorted_collector.values():
        final_iter.extend(i)
    
    print(final_iter)



lst=[1,2,34,45,45,44,5,6,8,3,25,6,5,74,34]

bucketSort(lst)

'''
Time Complexity is O(N^2) since we have used Insertion Sort
Space Complexity is O(N) since we are creating temporary dictionary for bucketing purpose

'''

    

'''
#Implementation of BUCKET SORT WITH NEGATIVE NUMBERS


#Bucket Sort with Negative Numbers

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    minValue = min(customList)
    maxValue = max(customList)
    rangeVal = (maxValue - minValue) / numberofBuckets
 
    buckets = [[] for _ in range(numberofBuckets)]
 
    for j in customList:
        if j == maxValue: #This is done in order to avoid index out of range error
            buckets[-1].append(j)
        else:
            index_b = math.floor((j - minValue) / rangeVal)
            buckets[index_b].append(j)
    
    sorted_array = []
    for i in range(numberofBuckets):
        buckets[i] = insertionSort(buckets[i])
        sorted_array.extend(buckets[i])
    
    return sorted_array

'''


