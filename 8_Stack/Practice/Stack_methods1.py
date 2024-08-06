#implementation of Stack using list (without size limit)

class Stack:
    #implementing the initializer
    def __init__(self):
        self.list=[]

    #implementing the print method
    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    #implementing isEmpty method
    def isEmpty(self):
        if self.list ==[]:
            return True
        else:
            return False
    
    #implementing the push method
    def push(self,value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    #implementing the pop method
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list.pop()
        
    #implementing peek method
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack"
        else:
            return self.list[-1]


    #implementing the delete method
    def delete(self):
        self.list=None


my_stack=Stack()

#my_stack.list=[1,2,4,5,56,7,77]

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack)

#print(my_stack.isEmpty())

#print(f'The popped element: {my_stack.pop()}')

#print(f'The result of peek method: {my_stack.peek()}')

my_stack.delete()
print(my_stack)

        