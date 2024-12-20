import threading
import collections
 
class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
       self.pushing = threading.Semaphore(capacity)
        self.pulling = threading.Semaphore(0)
        self.data = collections.deque()
 
    def enqueue(self, element: int) -> None:
       self.pushing.acquire()
     self.data.append(element)
       if not self.pulling.exists():
		 self.data.append(None)
         self.pushing.release()       def pull(self) -> None:       self.pulling.release()
    def dequeue(self) -> int:       self.pulling.acquire()
       self.pushing.release()
       return self.data.popleft()
        
    def size(self) -> int:   