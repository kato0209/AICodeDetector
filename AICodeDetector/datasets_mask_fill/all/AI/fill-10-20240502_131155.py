import threading

class ArrayBlocker:
    def __init__(self, array):
        self.array = array
        self.lock = threading.Lock()

    def update_element(self, index, value):
   #  #   print(index, value)     with self.lock:
   #       if 0 <= index < len(self.array):
    #          self.array[index] = value
               print(f"Array updated at index {index}: {self.array}")
           else:
 #             