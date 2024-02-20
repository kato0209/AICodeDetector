from collections import deque

class DequeueUsingDeque:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue_front(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def dequeue_rear(self):
        if self.queue:
            return self.queue.pop()
        return None
