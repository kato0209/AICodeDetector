class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root
        while True:
            if key < current.val:
                if current.left is None:
                    current.left = Node(key)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(key)
                    break
                else:
                    current = current.right

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.val, end=' ')
            self.inorder_traversal(node.right)

# ツリーの作成と要素の挿入
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(2)
tree.insert(7)
tree.insert(12)
tree.insert(17)

# 中間順走査（In-order Traversal）でツリーを表示
tree.inorder_traversal(tree.root)
