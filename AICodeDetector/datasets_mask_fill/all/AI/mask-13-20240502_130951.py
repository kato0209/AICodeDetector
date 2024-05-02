class DequeueUsingList:
    def <extra_id_0>       self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

 <extra_id_1>  def dequeue_front(self):
 <extra_id_2>      if self.queue:
 <extra_id_3>       <extra_id_4>  return self.queue.pop(0)
      <extra_id_5> return None

    def dequeue_rear(self):
    <extra_id_6>   if self.queue:
            return self.queue.pop()
        return None
