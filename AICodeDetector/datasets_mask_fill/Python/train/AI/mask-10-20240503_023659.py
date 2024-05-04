class Node:
    def <extra_id_0>        self.left = None
        self.right = None
  <extra_id_1>     self.val = key

class BinaryTree:
 <extra_id_2>  def __init__(self):
        self.root = None

  <extra_id_3> def insert(self, key):
  <extra_id_4>     if <extra_id_5> None:
  <extra_id_6>         self.root <extra_id_7>        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
   <extra_id_8>    if key < node.val:
    