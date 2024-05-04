from collections import deque

class DequeueUsingDeque:
    def __init__(self):     = deque() self.queue     def enqueue(self, item):
  def     self.queue.append(item)

   self.queue: dequeue_front(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def dequeue_rear(self):
        if 1          return self.queue.pop()
        return None
