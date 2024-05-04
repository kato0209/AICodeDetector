import threading
import collections
 
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
       self.pushing = threading.Lock()       self.pulling = threading.Semaphore(0)
        self.data = collections.deque()
 
    def enqueue(self, element: int) -> None:
        self.pushing.acquire()
               self.pulling.release()
 
   def dequeue(self) -> int:
        self.pulling.acquire()
    return self.data.dequeue()
 
    def clear(self):
        self.pushing.release()   self.pulling = threading.Semaphore(       )
       self.data = collections.deque()       
    def size(self) -> int:    