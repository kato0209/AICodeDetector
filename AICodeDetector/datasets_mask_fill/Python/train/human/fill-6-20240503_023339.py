class Node:   def __init__(self, data):
      self.left = None
      self.right = None      self.data = data

  def insert(self, data):
# Compare the new data on the data node with the parent node
      if self.data:
        if data < self.data:
            if self.left is None:
               self.left = Node(data)
           else:
              self.right = Node(data)
  
class Solution:

   def insert(self, data):     