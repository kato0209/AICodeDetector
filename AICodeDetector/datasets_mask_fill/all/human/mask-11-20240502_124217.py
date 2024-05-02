import threading
import collections
 
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
   <extra_id_0>    self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.data = collections.deque()
 
    def enqueue(self, element: int) -> None:
       <extra_id_1>    <extra_id_2>   <extra_id_3>       self.pulling.release()
 <extra_id_4>   def dequeue(self) -> <extra_id_5>       self.pulling.acquire()
  <extra_id_6>     self.pushing.release()
      <extra_id_7> return self.data.popleft()
        
    def size(self) -> <extra_id_8>   