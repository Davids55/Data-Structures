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

    



    def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

    ###################
    # Start Problem 2 #
    ###################
    def _contains(self, data, node):
        """
        This funciton will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if node is not None:
            if data < node.data:
                return self._contains(data, node.left)
            elif data > node.data:
                return self._contains(data, node.right)

            elif data == node.data:
                return True
        else:
            return False




tree = BST()
tree.insert(5)
tree.insert(3)
tree.insert(7)
# After implementing 'no duplicates' rule,
# this next insert will have no effect on the tree.
tree.insert(7)  
tree.insert(4)
tree.insert(9)
tree.insert(2)
tree.insert(6)


print("\n=========== PROBLEM 2 TESTS ===========")
print(3 in tree) # True
print(1 in tree) # False
