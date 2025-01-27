#Queue creation and methods (with a space constraint)
class Queue:
    def __init__(self,maxSize):
        self.items=[None]*maxSize
        self.maxSize=maxSize
        self.top=-1
        self.start=-1
    
    def __str__(self):
        collector=[str(x) for x in self.items]
        return ' '.join(collector)

    def isFull(self):
        if self.top + 1==self.start:
            return True
        elif self.start==0 and self.top+1==self.maxSize:
            return True
        else:
            return False
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            return 'Queue is full'
        else:
            if self.top+1==self.maxSize:
                self.top=0
            else:
                self.top+=1
                if self.start == -1:
                    self.start=0
            self.items[self.top]=value
            return "Value has been enqueued"
        
    def dequeue(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            firstElement=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
                self.top=-1
            elif self.start+1 == self.maxSize:
                self.start=0
            else:
                self.start+=1
            self.items[start]=None
            return firstElement
    
    def peek(self):
        if self.isEmpty():
            return 'The queue is empty'
        else:
            return self.items[self.start]
    
    def delete(self):
        self.items=[None]*self.maxSize
        self.top= -1
        self.start= -1


my_queue=Queue(6)
print(my_queue)

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
my_queue.enqueue(5)
my_queue.enqueue(6)

print(f'Peek into the first element of the queue: {my_queue.peek()}')

print('Post enqueueing: ')
print(my_queue)

print(my_queue.top,my_queue.start)
print(my_queue.enqueue(7))

print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())

print('Post dequeueing: ')
print(my_queue)


print(my_queue.delete())

print('Post deletion: ')
print(my_queue)




