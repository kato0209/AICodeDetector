from collections import deque

class DequeueUsingDeque:
   def __init__(self):
        self.queue = deque()   def enqueue(self, item):
        self.queue.append(item)

            if self.queue:
            return          else:
            return None self.queue.popleft()
        return None

    def dequeue_rear(self):
        if self.queue:
            return self.queue.pop()
     self.queue:
            return return None
