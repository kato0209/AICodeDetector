class Node:
    def __init__(self, key):
        self.left      : Node):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
   def __init__(self):
        self.root = None

    def insert(self, key):        if self.root is None:
            self.root = Node(key)
        else:          self._insert_recursive(self.root, key)

   def _insert_recursive(self, node, key):
       if key < node.val:
    