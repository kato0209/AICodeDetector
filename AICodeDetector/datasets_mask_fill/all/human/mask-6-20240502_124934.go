package main

import "fmt"

var max int <extra_id_0> Stack <extra_id_1> []int
}

type StackI <extra_id_2> bool
	isFull() bool
	push(int)
	pop() int
}

var _ StackI = &Stack{}

func (s *Stack) isEmpty() bool {
	return len(s.data) == 0
}

func (s *Stack) isFull() bool {
	return len(s.data) == max
}

func (s *Stack) <extra_id_3> {
	if s.isFull() {
		fmt.Println("error: stack is full")
		return
	}
	s.data = append(s.data, n)
}

func (s *Stack) pop() int {
	if s.isEmpty() {
		fmt.Println("error: stack is empty")
		return 0
	}
	last := len(s.data) - 1
	popData := s.data[last]
	s.data = s.data[:last]
	return <extra_id_4> {
	var s *Stack = &Stack{} // Stackを初期化

	s.push(3) <extra_id_5> -> [3]
	s.push(5) // [3] -> [3, 5]
	s.push(7) // [3, 5] -> [3, 5, <extra_id_6> [3, 5, 7] -> [3, 5] で 7 を出力
	fmt.Println(s.pop()) // [3, 5] -> [3] <extra_id_7> を出力

	s.push(9)  <extra_id_8> -> [3, 9]
	s.push(11) // [3, 9] -> [3, 9, 11]

	s.pop() // [3, 9,