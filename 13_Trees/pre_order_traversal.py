'''
Implementation of Pre-order traversal
Language: Python
'''


class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None



newBT=TreeNode("Drinks")
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")
newBT.leftChild=leftChild
newBT.rightChild=rightChild

def preOrderTraversal(rootNode):
    if not rootNode:    #---> O(1)
        return None
    print(rootNode.data) #---> O(1)
    
    preOrderTraversal(rootNode.leftChild) #---> O(n/2)
    preOrderTraversal(rootNode.rightChild) #---> O(n/2)

preOrderTraversal(newBT)


'''
Time Complexity: O(N)
Space Complexity: O(N) [worst case...when the tree is a linked list] | O(logN) [best case....when the tree is balanced]
'''

    
        