# Trees
Trees are the most complicated of the three that we will cover. Below is a visual representation of a Binary tree
just like a real tree there are branches that spread out from the original trunk (first node or root). each item in a tree is called a node and the node they are attached to is called the parent node. when trees have the same number of branches they are considered balanced just like the example below. keeping trees balanced makes searching and adding to them more efficient. a balanced tree has a O(log n) while a unbalanced tree is O(n).




![This is an image](https://github.com/Davids55/Data-Structures/blob/main/mceu_944294194111620741077326.jpg)


## Adding to and removing from a tree
Starting a BST(Binary search tree) takes a little bit more than placing brackets or curly brackets. take a look at the code below

```python
    class Node:
        
        def __init__(self, data):
           #creates the actual Tree
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        #tells python there is no root for the tree  
      
        self.root = None

    def insert(self, data):
    #this will make the first data entered into the root and force the rest to be child/branches
        
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root
```

next  we need the part that actually adds the data

```python
 def _insert(self, data, node):
        #if the data entered is larger thatn the root is   goes on the left   
        if data < node.data:
            
            if node.left is None:
                node.left = BST.Node(data)
            else:
               
                self._insert(data, node.left)
        
        #if the data entered is larger thatn the root is goes on the right
        elif data > node.data:
            
            
            if node.right is None:
                
                node.right = BST.Node(data)
            else:
                
                self._insert(data, node.right)
```
because of the way the tree is designed adding to a tree is O(log n) because it must search each subtree to find an available spot. Make sure you call  `name of the tree = BST()` to actually start the tree and use `.insert(value to add)` to add to your tree

Rather than show a lot more of the same code removing is very similar but instead you call `.remove(value to remove)`

## traverseing though a tree
We can have python go through a tree (aka traverse) and when code is written tell us the size (number of node) the height (number of layers our example above has a height of 3) or if it contains the wanted value. remember when you traverse a tree python will search every node.
1. `size()`    O(n)
2. `height()`   O(n)
3. `contains()`  O(log n)

## Example

lets go through this problem together.
lets say we want to create a tree and then add some values. we also want to find the hight of the tree.
lets start with what we know.


```python
class BST:
   

    class Node:
        
        def __init__(self, data):
           #creates the actual Tree
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        #tells python there is no root for the tree  
      
        self.root = None

    def insert(self, data):
    #this will make the first data entered into the root and force the rest to be child/branchs
        
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  

 
    def _insert(self, data, node):
  
        
        if data < node.data:
            
            if node.left is None:
               
                node.left = BST.Node(data)
            else:
                
                self._insert(data, node.left)
        
        
        elif data > node.data:
            
            
            if node.right is None:
               
                node.right = BST.Node(data)
            else:
                
                self._insert(data, node.right)
                
# bewlow this is what you would do to get the height of the tree
    
    def get_height(self):
        
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root
    
    
    def _get_height(self, node):

        if node is None:
            return 0
        else:
            return max(self._get_height(node.left), self._get_height(node.right)) + 1

    

# data we will be inserting

tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(3)
tree.insert(7)  
tree.insert(4)
tree.insert(10)
tree.insert(1)
tree.insert(6)

print(tree.get_height())
```
you should get three as your answer here is a model of what the tree would look like. 


# Problem
Your problem to try is to find data if a certain number is in the tree for this problem use the code we ran above to create the tree.
try to see if 2 and three are in the tree

solution[]




[back to home](https://github.com/Davids55/Data-Structures)
