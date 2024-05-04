class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
     <extra_id_0>  self.val = key

class BinaryTree:
    def __init__(self):
 <extra_id_1>  <extra_id_2>   self.root = None

    def insert(self, key):
     <extra_id_3>  if self.root is None:
   <extra_id_4>      <extra_id_5> self.root = Node(key)
 <extra_id_6>          return

        <extra_id_7> self.root
        while True:
   <extra_id_8>        if