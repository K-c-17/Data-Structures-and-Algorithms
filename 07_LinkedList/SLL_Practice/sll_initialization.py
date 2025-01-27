#Initializing a node

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

#Linked list with one node
class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node #define the head attribute of that LL object
        self.tail=new_node #define the tail attribute of that LL object
        self.length=1 #define the size of this LL


#Creating a Linked List with just one node. So, Head is that node and tail is also that node
ll1=LinkedList(2)

print(ll1) #prints the location of that ll in memory
print(ll1.head) #prints head node
print(ll1.tail) #prints tail node
print(ll1.length) #prints the size of your LL

#How to print the values of tail and head
print(ll1.tail.value) #This prints the value attribute of the node that is referred as head
print(ll1.tail.value) #This prints the value attribute of the nod ethat is referred as tail

