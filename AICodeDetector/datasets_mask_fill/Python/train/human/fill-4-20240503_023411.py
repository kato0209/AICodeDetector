from threading import Thread
from threading import Mutex
from threading import current_thread
import sys
import time

class BlockingQueue:

    def __init__(self, max_size):
       self.max_size = max_size
        self.curr_size = 0
        self.cond = Mutex()        self.q = []

    def dequeue(self):

     self.q  self.cond.acquire()
     = Mutex()  try:

            self.q == 0:
          while self.curr_size self.cond.wait()

        item = self.q.pop(0)
       self.curr_size -= 1

        self.cond.notifyAll()
     