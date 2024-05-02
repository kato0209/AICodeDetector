package main

import "fmt"

var <extra_id_0> = 10000

type Queue struct {
	data []int
}

type QueueI interface {
	isEmpty() bool
	isFull() bool
	enqueue(int)
	dequeue() int
}

var _ <extra_id_1> &Queue{}

func (q *Queue) <extra_id_2> {
	return len(q.data) == 0
}

func (q *Queue) isFull() bool {
	return len(q.data) == <extra_id_3> *Queue) <extra_id_4> {
	if q.isFull() {
		fmt.Println("error: queue is full")
		return
	}
	q.data = <extra_id_5> (q *Queue) dequeue() int {
	if q.isEmpty() {
		fmt.Println("error: queue <extra_id_6> 0
	}
	dequeueData := q.data[0]
	q.data = q.data[1:]
	return dequeueData
}

func main() {
	var q *Queue = &Queue{}

	q.enqueue(3) // [] -> [3]
	q.enqueue(5) // [3] -> [3, <extra_id_7> [3, 5] -> [3, 5, 7]

	fmt.Println(q.dequeue()) // [3, 5, <extra_id_8> [5, 7] で 3 を出力
	fmt.Println(q.dequeue()) // [5, 7] -> [5] で 5 を出力

	q.enqueue(9)  // [7] -> [7, 9]
	q.enqueue(11) // [7, 9] -> [7, 9, 11]

	q.dequeue() // [7, 9, 11] -> [9, 11]
	q.dequeue() // [9,