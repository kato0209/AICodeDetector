import threading

class ArrayBlocker:
    def __init__(self, array):
        self.array = array
        self.lock = threading.Lock()

    def update_element(self, <extra_id_0>  <extra_id_1>     with self.lock:
   <extra_id_2>     <extra_id_3>  if 0 <= index < len(self.array):
    <extra_id_4>         <extra_id_5> self.array[index] = value
         <extra_id_6>      print(f"Array updated at index {index}: {self.array}")
       <extra_id_7>    else:
 <extra_id_8>             