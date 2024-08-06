class Node:
    def __init__(self, value):
        self.value=value
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    #Printing a LinkedList using ___str__ method
    def __str__(self): 
        result=''
        temp_node=self.head
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+=' --> '
            temp_node=temp_node.next
        return result
    
    #Appending a node to the existing list
    def append(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
    
    #Prepend a node to an existing linked list
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length+=1

    

#Print statement
sll=LinkedList()
sll.append(1)
sll.append(2)
sll.append(3)


print(f'The head of this sll is {sll.head.value}')
print(f'The tail of this sll is {sll.tail.value}')
print(f'The length of this sll is {sll.tail.value}')
print(sll)

sll.prepend(0)
sll.prepend(-1)
sll.prepend(-2)

print(f'Post prepend operation head of this sll is {sll.head.value}')
print(f'Post prepend operation tail of this sll is {sll.tail.value}')
print(f'Post prepend operation length of this sll is {sll.tail.value}')
print(sll)
