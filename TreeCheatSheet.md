
---

# 📜 **Cheatsheet: Tree and Graph Implementations with Traversals**

## 🌲 **Binary Tree Basics**

### Binary Tree Node Class
```python
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

### Common Operations
#### Insert a Node
```python
def insert_node(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root
```

---

## 🌲 **Tree Traversals**

### **1. Preorder Traversal (Root -> Left -> Right)**
#### Recursive
```python
def preorder_traversal(root):
    if root:
        print(root.value, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)
```
#### Iterative
```python
def preorder_iterative(root):
    stack = [root]
    while stack:
        current = stack.pop()
        print(current.value, end=" ")
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
```

---

### **2. Inorder Traversal (Left -> Root -> Right)**
#### Recursive
```python
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)
```
#### Iterative
```python
def inorder_iterative(root):
    stack, current = [], root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.value, end=" ")
        current = current.right
```

---

### **3. Postorder Traversal (Left -> Right -> Root)**
#### Recursive
```python
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.value, end=" ")
```
#### Iterative
```python
def postorder_iterative(root):
    stack, output = [root], []
    while stack:
        current = stack.pop()
        output.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    print(" ".join(map(str, output[::-1])))
```

---

### **4. Level Order Traversal (BFS for Trees)**
```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        current = queue.popleft()
        print(current.value, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
```

---

## 🌲 **Binary Search Tree (BST) Operations**

### Search a Node
```python
def search_bst(root, value):
    if not root or root.value == value:
        return root
    if value < root.value:
        return search_bst(root.left, value)
    return search_bst(root.right, value)
```

### Delete a Node
```python
def delete_node(root, value):
    if not root:
        return root
    if value < root.value:
        root.left = delete_node(root.left, value)
    elif value > root.value:
        root.right = delete_node(root.right, value)
    else:
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        min_larger_node = find_min(root.right)
        root.value = min_larger_node.value
        root.right = delete_node(root.right, min_larger_node.value)
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
```

---

## 🌐 **Graph Basics**

### Graph Representation

#### Adjacency List
```python
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)

    def print_graph(self):
        for vertex, edges in self.adjacency_list.items():
            print(f"{vertex}: {edges}")
```

#### Example Usage
```python
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_edge("A", "B")
g.print_graph()
```

---

## 🌐 **Graph Traversals**

### **1. Breadth-First Search (BFS)**
```python
from collections import deque

def bfs(graph, start_vertex):
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)

    while queue:
        current = queue.popleft()
        print(current, end=" ")
        for neighbor in graph.adjacency_list[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

---

### **2. Depth-First Search (DFS)**
#### Iterative
```python
def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]

    while stack:
        current = stack.pop()
        if current not in visited:
            print(current, end=" ")
            visited.add(current)
            for neighbor in graph.adjacency_list[current]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

#### Recursive
```python
def dfs_recursive(graph, vertex, visited=set()):
    if vertex not in visited:
        print(vertex, end=" ")
        visited.add(vertex)
        for neighbor in graph.adjacency_list[vertex]:
            dfs_recursive(graph, neighbor, visited)
```

---

## 🔑 **Key Tips for Revision**

1. **Tree Traversals**:
   - **Preorder**: Root -> Left -> Right
   - **Inorder**: Left -> Root -> Right
   - **Postorder**: Left -> Right -> Root
   - **Level Order**: BFS

2. **Graph Traversals**:
   - **BFS**: Use a **queue**, visit nodes level-by-level.
   - **DFS**: Use a **stack** (or recursion), explore deep paths first.

3. **Code Daily**: Write each traversal algorithm every day from memory.
4. **Solve Easy Problems**:
   - Trees: [LeetCode #94](https://leetcode.com/problems/binary-tree-inorder-traversal/), [#144](https://leetcode.com/problems/binary-tree-preorder-traversal/)
   - Graphs: [LeetCode #133](https://leetcode.com/problems/clone-graph/), [#200](https://leetcode.com/problems/number-of-islands/)

5. **Practice Edge Cases**:
   - Empty tree/graph.
   - Single-node tree/graph.
   - Unbalanced trees.
   - Cyclic vs. acyclic graphs.

---

## 🚀 **Next Steps**
1. Revise this cheatsheet daily.
2. Implement these methods from scratch.
3. Solve 3-5 problems on LeetCode daily, focusing on traversal and graph problems.

This cheat sheet covers essential details to solidify your understanding. Let me know if you want further elaborations or additional examples!