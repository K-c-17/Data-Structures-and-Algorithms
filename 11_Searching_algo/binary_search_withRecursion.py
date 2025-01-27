'''
Implementation of Binary Search with Recursion in Python
'''


def binary_search(arr, left, right, target):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, mid + 1, right, target)
    else:
        return binary_search(arr, left, mid - 1, target)




'''
Time Complexity: Each call halves the size of the search space. The recurrence relation is T(n) = T(n/2) + O(1), which results in O(log n) time complexity.
Space Complexity: The depth of recursion is log n (as each call reduces the problem size by half), resulting in O(log n) space complexity.
'''
