from collections import deque

class DequeueUsingDeque:
    def <extra_id_0>     <extra_id_1> self.queue <extra_id_2>    def enqueue(self, item):
  <extra_id_3>     self.queue.append(item)

   <extra_id_4> dequeue_front(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def dequeue_rear(self):
        if <extra_id_5>         <extra_id_6> return self.queue.pop()
        return None
