<extra_id_0>   def __init__(self, data):
      self.left <extra_id_1>      self.right = None
     <extra_id_2> = data

   def insert(self, data):
# Compare the new value with the parent <extra_id_3>     if self.data:
         if data < self.data:
      <extra_id_4>     if self.left is None:
           <extra_id_5>   <extra_id_6> Node(data)
      <extra_id_7>     else:
              <extra_id_8>      