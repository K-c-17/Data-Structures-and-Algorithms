#implementation of Stack using list (with size limit)

class Stack:
    #implementing the initializer
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.list=[]

    #implementing the print method
    def __str__(self):
        values=[str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    #implementing the isEmpty method
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    #implementing the isFull method since in this stack there is a size constraint
    def isFull(self):
        if len(self.list)==self.maxSize:
            return True
        else:
            return False
    
    #implementing the push() method 
    def push(self,value):
        if self.isFull():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"
    
    #implementing the pop method
    def pop(self):
        if self.isEmpty():
            return "There is nothing in stack"
        else:
            return self.list.pop()
    
    #implementing the peek method
    def peek(self):
        if self.isEmpty():
            return "There is nothing in stack"
        else:
            return self.list[len(self.length)-1]
    
    #implementing the delete method
    def delete(self):
        self.list=None
    
    
my_stack=Stack(4)               #setting the maximum size to 4
print(my_stack.isEmpty())
print(my_stack.isFull())
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
print(my_stack.push(5))
print(my_stack)
print(my_stack.maxSize)