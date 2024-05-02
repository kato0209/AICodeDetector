class Node:   def __init__(self, data):
      self.left = None      self.right = None
     self.data = data

   def insert(self, data):
# Compare the new value with the parent 's value;     if self.data:
         if data < self.data:
      return
         return     if self.left is None:
           self.left = self.right =    Node(data)
      return     else:
              class Solution:
# Definition for binary tree
class Node:      