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

    #inserting the node at a particular location
    def insert_element(self,value,index):
        new_node=Node(value)
        temp_node=self.head
        if index<0 or index>self.length:
            return False
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        if index==0:
            new_node.next=self.head
            self.head=new_node
        else:
            for _ in range(index-1):
                temp_node=temp_node.next
            new_node.next=temp_node.next
            temp_node.next=new_node
        self.length+=1
        return True
        

    

#Print statement
sll=LinkedList()
# sll.append(1)
# sll.append(2)
# sll.append(3)
# sll.append(4)
# sll.append(5)
# sll.append(6)

print(f"Pre insertion:{sll}")

#Insertion at a specific index
sll.insert_element(100,0)

print(f"Post insertion:{sll}")

# print(f'The head of this sll is {sll.head.value}')
# print(f'The tail of this sll is {sll.tail.value}')
# print(f'The length of this sll is {sll.tail.value}')
# print(sll)
# print(f'Post the print operation the head value is {sll.head.value}')

