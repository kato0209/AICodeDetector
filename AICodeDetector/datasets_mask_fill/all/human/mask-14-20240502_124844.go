package main

import "fmt"

type Queue struct {
  <extra_id_0> List []int
}

// function to add element in queue
func (q *Queue) Enqueue(element int) {
    q.List = append(q.List, element)
}

// function to delete element <extra_id_1> queue
func (q *Queue) <extra_id_2> {
    if q.isEmpty() {
        fmt.Println("Queue is empty.")
  <extra_id_3>     return 0
 <extra_id_4>  }
    element := q.List[0]
    q.List = q.List[1:]

    return element
}

// function check that queue <extra_id_5> or not
func (q *Queue) isEmpty() bool {
    return len(q.List) == <extra_id_6> is a function with matrix and int value as parameter
func BFS(graph <extra_id_7> int) <extra_id_8>   // initializing