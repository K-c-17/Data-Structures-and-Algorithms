class Node:
    def __init__(self, value):
        self.value=value
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1


sll=LinkedList()
sll.append(1)
sll.append(2)
sll.append(3)

print(f'The head of this sll is {sll.head.value}')
print(f'The tail of this sll is {sll.tail.value}')
print(f'The length of this sll is {sll.tail.value}')

