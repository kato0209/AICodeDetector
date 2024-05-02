from collections import deque

class DequeueUsingDeque:
   <extra_id_0> __init__(self):
        self.queue = <extra_id_1>   def enqueue(self, item):
        self.queue.append(item)

    <extra_id_2>        if <extra_id_3>          <extra_id_4> self.queue.popleft()
        return None

    def dequeue_rear(self):
        if self.queue:
            return self.queue.pop()
 <extra_id_5>    <extra_id_6> return None
