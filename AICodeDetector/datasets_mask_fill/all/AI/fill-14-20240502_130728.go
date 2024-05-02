
package main

type Queue []int

// Enqueue adds an element to the end of the Queue.
func (q *Queue) Enqueue(value int) {    *q = append(*q, value)
}

// Dequeue removes the first element of the queue and returns it.
func (q *Queue) Dequeue() (int, bool) {
    if len(*q) == 0 {
        return 0, false
    }
    element := (*q)[0]
    *q = (*q)[1:]
    return element, true
}

func main() {
   var q Queue

    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)

    if element, ok := q.Dequeue(); ok {
        // Use element
  instead of queue to test stack overflow.  