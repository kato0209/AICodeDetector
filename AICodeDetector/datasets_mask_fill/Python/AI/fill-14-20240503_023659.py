class Queue():    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def dequeue_front(self):
        if self.queue:            return self.queue.pop(0)
        return None

    def dequeue_back(self):       if self.queue:
           return self.queue.pop()
     def front(self):  return None
