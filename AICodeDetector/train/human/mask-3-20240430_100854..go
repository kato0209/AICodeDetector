package main

import "fmt"

var max int = 10000

type <extra_id_0> {
	data []int
}

type QueueI interface {
	isEmpty() bool
	isFull() bool
	enqueue(int)
	dequeue() int
}

var _ QueueI = <extra_id_1> *Queue) isEmpty() bool {
	return len(q.data) == 0
}

func (q *Queue) isFull() bool {
	return len(q.data) == max
}

func (q <extra_id_2> int) {
	if q.isFull() {
		fmt.Println("error: queue is full")
		return
	}
	q.data = append(q.data, n)
}

func (q *Queue) dequeue() int {
	if q.isEmpty() {
		fmt.Println("error: <extra_id_3> empty")
		return 0
	}
	dequeueData := q.data[0]
	q.data = <extra_id_4> main() {
	var q *Queue = &Queue{}

	q.enqueue(3) // [] -> <extra_id_5> [3] -> [3, 5]
	q.enqueue(7) // [3, 5] -> [3, 5, 7]

	fmt.Println(q.dequeue()) // [3, 5, 7] -> [5, 7] で 3 を出力
	fmt.Println(q.dequeue()) // [5, 7] -> [5] <extra_id_6> を出力

	q.enqueue(9)  // [7] -> [7, 9]
	q.enqueue(11) <extra_id_7> 9] -> [7, 9, 11]

	q.dequeue() // [7, 9, <extra_id_8> [9, 11]
	q.dequeue() // [9,