from threading import Thread
from threading import Condition
from threading import current_thread
import <extra_id_0> BlockingQueue:

    def __init__(self, max_size):
      <extra_id_1> self.max_size = max_size
   <extra_id_2>    self.curr_size = 0
        self.cond = Condition()
        self.q = <extra_id_3>   def dequeue(self):

     <extra_id_4>  <extra_id_5>       while self.curr_size == 0:
   <extra_id_6>       <extra_id_7>        item = self.q.pop(0)
        self.curr_size -= 1

    <extra_id_8>   self.cond.notifyAll()
     