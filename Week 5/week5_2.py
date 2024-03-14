class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.ismirrored = False


    def insert(self, key):
        if self.ismirrored is True:
            self.mirror()
            self.root = self.insert_recursion(self.root, key)
            self.mirror()
        else:
            self.root = self.insert_recursion(self.root, key)
        return
    
    def insert_recursion(self, node, key):
        if node == None:
            node = Node(key)
        elif node.key > key:
            node.left = self.insert_recursion(node.left, key)
        elif node.key < key:
            node.right = self.insert_recursion(node.right, key)
        return node
    
    def preorder(self):
        self.preorder_recursion(self.root)
        print()
        return
    
    def preorder_recursion(self, node):
        print(node.key, end=" ")
        if node.left:
            self.preorder_recursion(node.left)
        if node.right:
            self.preorder_recursion(node.right)

    def search(self, key):
        if self.ismirrored is True:
            self.mirror()
            factor = self.search_recursion(self.root, key)
            self.mirror()
            return factor
        else:
            return self.search_recursion(self.root, key)

    def search_recursion(self, node, key):
        if node is None:
            return False
        elif node.key > key:
            return self.search_recursion(node.left, key)
        elif node.key < key:
            return self.search_recursion(node.right, key)
        else:
            return True
        
    def remove(self, key):
        if self.ismirrored is True:
            self.mirror()
            self.remove_recursion(self.root, key)
            self.mirror()
        else:
            self.remove_recursion(self.root, key)

    def remove_recursion(self, node, key):
        if node is None:
            return None
        elif key > node.key:
            node.right = self.remove_recursion(node.right, key)
        elif key < node.key:
            node.left = self.remove_recursion(node.left, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self.getmax(node.left)
                node.left = self.removemax(node.left)
        return node
        
    def getmax(self, node):
        if node.right is None:
            return node.key
        else:
            return self.getmax(node.right)
        
    def removemax(self, node):
        if node.right is None:
            return node.left
        node.right = self.removemax(node.right)
        return node
    
    def postorder(self):
        self.postorder_recursion(self.root)
        print()
        return
    
    def postorder_recursion(self, node):
        if node.left is not None:
            self.postorder_recursion(node.left)
        if node.right is not None:
            self.postorder_recursion(node.right)
        print(node.key, end=" ")
        return node

    def inorder(self):
        self.inorder_recursion(self.root)
        print()
    
    def inorder_recursion(self, node):
        if node.left is not None:
            self.inorder_recursion(node.left)
        print(node.key, end=" ")
        if node.right is not None:
            self.inorder_recursion(node.right)
        return node

    def breadthfirst(self):
        node = self.root
        queue = []
        if node is not None:
            queue.append(node)
        while len(queue) > 0:
            print(queue[0].key, end=" ")
            node = queue[0]
            del queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def mirror(self):
        node = self.root
        queue = []
        if node is not None:
            queue.append(node)
        while len(queue) > 0 :
            node = queue[0]
            node.left, node.right = node.right, node.left
            del queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if self.ismirrored is False:
            self.ismirrored = True
        else:
            self.ismirrored = False


if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
    Tree.mirror()
    Tree.preorder()         # 5 9 7 6 1 3 4 2

    Tree.insert(8)
    Tree.remove(3)
    print(Tree.search(2))   # True
    Tree.preorder()         # 5 9 7 8 6 1 2 4
    Tree.mirror()
    Tree.preorder()         # 5 1 2 4 9 7 6 8

