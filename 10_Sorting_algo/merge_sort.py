'''
Implementation of Merge Sort
Language: Python
'''

# Merge Sort

def mergeSort(arr):

  print("Input: ", arr)
  if len(arr)<=1:
    print("Output1: ", arr)
    return arr
  # f = 0
  # l = len(arr)
  mid = len(arr)//2

  left = arr[:mid]
  right = arr[mid:]
  # left[0]= -2

  print("Left:",left)
  print("Right:",right)
  left = mergeSort(left)
  right = mergeSort(right)
  print("Merge: ", left, right)
  merged_array = [0] * len(arr)
  i=j=k=0

  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      merged_array[k] = left[i]
      i += 1
    else:
      merged_array[k] = right[j]
      j += 1
    k += 1

  while i< len(left):
    merged_array[k]=left[i]
    i += 1
    k += 1
  while j< len(right):
    merged_array[k]=right[j]
    j += 1
    k +=1
  print("Output2: ", merged_array)
  return merged_array




array = [10,2,9,4,18,32,0,-1]
merged_array = mergeSort(array)
print(merged_array)