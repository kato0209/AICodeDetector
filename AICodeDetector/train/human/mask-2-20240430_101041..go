package main

import "fmt"

var max int <extra_id_0> Stack struct {
	data []int
}

type StackI interface {
	isEmpty() bool
	isFull() bool
	push(int)
	pop() int
}

var _ StackI = &Stack{}

func (s *Stack) <extra_id_1> {
	return len(s.data) == 0
}

func (s *Stack) isFull() bool {
	return len(s.data) == max
}

func (s *Stack) push(n <extra_id_2> s.isFull() {
		fmt.Println("error: stack is full")
		return
	}
	s.data = append(s.data, n)
}

func <extra_id_3> pop() int {
	if s.isEmpty() {
		fmt.Println("error: stack is empty")
		return 0
	}
	last := len(s.data) - 1
	popData := s.data[last]
	s.data = <extra_id_4> main() {
	var s *Stack <extra_id_5> // Stackを初期化

	s.push(3) // [] -> [3]
	s.push(5) // [3] -> [3, 5]
	s.push(7) // [3, 5] -> [3, <extra_id_6> // [3, 5, 7] -> [3, 5] で 7 を出力
	fmt.Println(s.pop()) // [3, 5] -> [3] で 5 を出力

	s.push(9)  // [3] <extra_id_7> 9]
	s.push(11) // <extra_id_8> -> [3, 9, 11]

	s.pop() // [3, 9,