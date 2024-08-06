#Creation of Stack using a linked list

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

class Stack:
    def __init__(self):
        self.LinekdList=LinkedList()

