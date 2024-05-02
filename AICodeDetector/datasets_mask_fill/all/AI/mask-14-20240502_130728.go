
package main

type Queue []int

// Enqueue adds an <extra_id_0> the end of the <extra_id_1> *Queue) Enqueue(value <extra_id_2>    *q = append(*q, value)
}

// Dequeue removes <extra_id_3> element of <extra_id_4> and returns <extra_id_5> *Queue) Dequeue() (int, bool) {
    if len(*q) <extra_id_6> {
        return 0, false
    }
    element := (*q)[0]
    *q = (*q)[1:]
    return element, true
}

func main() {
   <extra_id_7> q Queue

    q.Enqueue(1)
    q.Enqueue(2)
    q.Enqueue(3)

    if element, ok := q.Dequeue(); ok {
        // Use element
  <extra_id_8>  