#Queue Creation and methods (without size constraint)

class Queue:
    def __init__(self):
        self.items=[]
    
    def __str__(self):
        collector=[str(x) for x in self.items]
        return ' '.join(collector)
    
    def isEmpty(self):
        if self.items==[]:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.items.append(value)
        return "The element is inserted in the end of the queue"
    
    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            return self.items.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items= None


my_queue=Queue()

print('Insertion in the queue')
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)
print('Post insertion queue:')
print(my_queue)

print('Popping element from the queue:')
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print('Post popping queue:')
print(my_queue)

print(f'Taking a peek in the queue: {my_queue.peek()}')


