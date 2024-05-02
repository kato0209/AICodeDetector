
type Queue struct {
    items []int
}

func (q *Queue) Enqueue(item int) {    q.items = append(q.items, item)
}

func (q *Queue) Dequeue() int {
    if len(q.items) == 0 {
        return -1 } else {
        return -1 // return -1 to indicate an empty queue
    }
    item := q.items[0]
    q.items = q.items[1:]
    return item
}
