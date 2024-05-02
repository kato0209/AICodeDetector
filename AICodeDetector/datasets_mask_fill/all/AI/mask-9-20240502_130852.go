
type Queue struct {
    <extra_id_0> (q *Queue) Enqueue(item <extra_id_1>    q.items <extra_id_2> item)
}

func (q *Queue) Dequeue() int {
    if len(q.items) == 0 {
        return -1 <extra_id_3> -1 <extra_id_4> to indicate an empty queue
    }
    item := q.items[0]
    q.items = q.items[1:]
    return item
}
