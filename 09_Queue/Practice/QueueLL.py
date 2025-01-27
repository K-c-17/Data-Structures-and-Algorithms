#Creation and implementing operations on Linked List based queues

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
    
    def __str__(self):
        return str(self.value)

    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    #creating an iter function so that we can implement print method in our queue
    def __iter__(self):
        curr=self.head
        while curr:
            yield curr
            curr=curr.next

class Queue:
    def __init__(self):
        self.linkedList=LinkedList()

    def __str__(self):
        collector=[str(x.value) for x in self.linkedList]       #use of the iter function in the Node class
        return ' '.join(collector)
    
    def isEmpty(self):
        if not self.linkedList.head:
            return True
        else:
            return False
    
    def enqueue(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.linkedList.head=new_node
            self.linkedList.tail=new_node
        else:
            self.linkedList.tail.next=new_node
            self.linkedList.tail=new_node
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            first_node=self.linkedList.head
            if self.linkedList.head==self.linkedList.tail:
                self.linkedList.head=None
                self.linkedList.tail=None
            else:
                self.linkedList.head=first_node.next
                first_node.next=None
            return first_node
    
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            return self.linkedList.head.value
        
    def delete(self):
        self.linkedList.head=None
        self.linkedList.tail=None
    

my_queue=Queue()

#adding element in the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)


print(my_queue)
#removing elements from the queue
print(my_queue.dequeue())
print(my_queue.dequeue())

print('Printing queue post removal:')
print(my_queue)

#deletion of entire row:
my_queue.delete()

print('Printing queue post deletion:')
print(my_queue)


        


    
    