#Creation of Stack using a linked list

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()            #part responsible for creation of stack usign linked list

    def __str__(self):
        collector=[str(x.value) for x in self.LinkedList]
        return '\n'.join(collector)             #here you don't need to reverse the collector since the head of the linked list is already the "last in" element
    
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
        
    def push(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.LinkedList.head=new_node
        else:
            new_node.next=self.LinkedList.head
            self.LinkedList.head=new_node
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            popped_node=self.LinkedList.head
            self.LinkedList.head=popped_node.next
            popped_node.next=None
            return popped_node.value
        
    def peek(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.LinkedList.head.value
    
    def delete(self):
        self.LinkedList.head=None




my_stack=Stack()

print(my_stack.isEmpty())           #Checking if the stack is empty

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)

print(my_stack)                     #printing the stack post 5 pushes

print(f'The popped value from stack: {my_stack.pop()}')

print(my_stack)

print(f'The first element of the stack is : {my_stack.peek()}')





