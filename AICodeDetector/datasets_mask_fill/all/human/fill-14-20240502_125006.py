from threading import Thread
from threading import Condition
from threading import current_thread
import time

class BlockingQueue:

    def __init__(self, max_size):
       self.max_size = max_size
       self.curr_size = 0
        self.cond = Condition()
        self.q = []   def dequeue(self):

              while self.curr_size == 0:
   print "\n\t"
		    self.cond.wait               item = self.q.pop(0)
        self.curr_size -= 1

    return item   self.cond.notifyAll()
     