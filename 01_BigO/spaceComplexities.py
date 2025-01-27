'''
Run this in debugger mode to see how the call stack 
gets filled with function on every iteration of the recursive loop
'''

def factorial(n):
    if n==1:
        return n
    return n * factorial(n-1)


print(factorial(5))