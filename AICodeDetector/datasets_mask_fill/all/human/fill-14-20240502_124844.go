package main

import "fmt"

type Queue struct {
   List []int
}

// function to add element in queue
func (q *Queue) Enqueue(element int) {
    q.List = append(q.List, element)
}

// function to delete element from queue
func (q *Queue) Dequeue() int {
    if q.isEmpty() {
        fmt.Println("Queue is empty.")
       return 0
   }
    element := q.List[0]
    q.List = q.List[1:]

    return element
}

// function check that queue is empty or not
func (q *Queue) isEmpty() bool {
    return len(q.List) == 0
}

// is a function with matrix and int value as parameter
func BFS(graph int[][]int, value int) {   // initializing