#implementation of Stack using list (without size limit)

class Stack:
    #implementing the initializer
    def __init__(self):
        self.list=[]

    #implementing the print method
    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return '\n'.join(values)


my_stack=Stack()

my_stack.list=[1,2,4,5,56,7,77]

print(my_stack)
        