from threading import Thread
from threading import <extra_id_0> import current_thread
import <extra_id_1> BlockingQueue:

    def __init__(self, max_size):
     <extra_id_2>  self.max_size = max_size
        self.curr_size = 0
        self.cond <extra_id_3>        self.q = []

    def dequeue(self):

     <extra_id_4>  self.cond.acquire()
     <extra_id_5>  <extra_id_6> == 0:
          <extra_id_7> self.cond.wait()

        item = self.q.pop(0)
   <extra_id_8>    self.curr_size -= 1

        self.cond.notifyAll()
     