import threading

class ArrayBlocker:
    def __init__(self, array):
    <extra_id_0>   self.array <extra_id_1>        self.lock = threading.Lock()

    def update_element(self, index, value):
       <extra_id_2> self.lock:
            if 0 <= index < <extra_id_3>           <extra_id_4>  <extra_id_5> = value
               <extra_id_6> updated at <extra_id_7> {self.array}")
            else:
  <extra_id_8>            