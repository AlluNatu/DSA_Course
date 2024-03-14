class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None
        self.balance = 0

class AVL:
    def __init__(self) -> None:
        self.root = None
        self.is_balanced = True


    def insert(self, key: int):
        self.root = self.insert_help(self.root, key)
         

    def insert_help(self, root, key):
        if not root:
            root = AVLNode(key)
            self.is_balanced = False
        elif key < root.key:
            root.left = self.insert_help(root.left, key)
            if not self.is_balanced:                           
                if root.balance >= 0:                       
                    self.is_balanced = root.balance == 1
                    root.balance -= 1
                else:                                       
                    if root.left.balance == -1:
                        root = self.right_rotation(root)    
                    else:
                        root = self.left_right_rotation(root)   
                    self.is_balanced = True

        elif key > root.key:
            root.right = self.insert_help(root.right, key)
            if not self.is_balanced:                           
                if root.balance <= 0:                       
                    self.is_balanced = root.balance == -1
                    root.balance += 1
                else:                                       
                    if root.right.balance == 1:
                        root = self.left_rotation(root)   
                    else:
                        root = self.right_left_rotation(root)   
                    self.is_balanced = True
        return root
    
    def right_rotation(self, root):
        child = root.left                   
        root.left = child.right             
        child.right = root
        child.balance = root.balance = 0    
        return child
    
    def left_rotation(self, root):
        child = root.right                   
        root.right = child.left             
        child.left = root
        child.balance = root.balance = 0    
        return child
    
    def left_right_rotation(self, root: AVLNode):
        child = root.left
        grandchild = child.right            
        child.right = grandchild.left       
        grandchild.left = child
        root.left = grandchild.right
        grandchild.right = root
        root.balance = child.balance = 0    
        if grandchild.balance == -1:
            root.balance = 1 
        elif grandchild.balance == 1:
            child.balance = -1
        grandchild.balance = 0
        return grandchild
    
    def right_left_rotation(self, root: AVLNode):
        child = root.right
        grandchild = child.left            
        child.left = grandchild.right       
        grandchild.right = child
        root.right = grandchild.left
        grandchild.left = root
        root.balance = child.balance = 0
        if grandchild.balance == 1:
            root.balance = -1 
        elif grandchild.balance == -1:
            child.balance = 1
        grandchild.balance = 0
        return grandchild
    
    def preorder(self):
        self.preorder_recursion(self.root)
        print()
        return
    
    def preorder_recursion(self, node):
        print(str(node.key) + ";" + str(node.balance), end=" ")
        if node.left:
            self.preorder_recursion(node.left)
        if node.right:
            self.preorder_recursion(node.right)
    


if __name__ == "__main__":
    Tree = AVL()
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
        Tree.insert(key)
    Tree.preorder()