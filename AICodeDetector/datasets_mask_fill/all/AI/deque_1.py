class DequeueUsingList:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue_front(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def dequeue_rear(self):
        if self.queue:
            return self.queue.pop()
        return None
