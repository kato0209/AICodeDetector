import threading
import collections
 
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
      <extra_id_0> self.pushing = <extra_id_1>       self.pulling = threading.Semaphore(0)
        self.data = collections.deque()
 
    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
        <extra_id_2>       self.pulling.release()
 
  <extra_id_3> def dequeue(self) -> int:
        self.pulling.acquire()
    <extra_id_4>   <extra_id_5>       <extra_id_6>     <extra_id_7>  
    def size(self) <extra_id_8>    