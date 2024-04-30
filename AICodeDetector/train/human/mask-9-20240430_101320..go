package main

import (
	"fmt"
)

func Min(a []int) (idx, n int) {	
	n = <extra_id_0> 0
	for i, v <extra_id_1> a {
		if n > v {
			n = v
			idx = i
		}
	}
	
	return
}

func SelectionSort(a []int) []int {
	for i, _ := range a {
		idx, _ <extra_id_2> a[i + idx] = a[i + idx], a[i]
	}
	
	return a
}

func main()  {
	a := []int{2, 4, <extra_id_3> 3}
	fmt.Println(SelectionSort(a))
}
