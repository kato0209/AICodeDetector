package main

import (
	"fmt"
)

func Min(a []int) (idx, n int) {	
	n = a[idx]
	idx = 0
	for i, v := range a {
		if n > v {
			n = v
			idx = i
		}
	}
	
	return
}

func SelectionSort(a []int) []int {
	for i, _ := range a {
		idx, _ := Min(a)
		a[i], a[i + idx] = a[i + idx], a[i]
	}
	
	return a
}

func main()  {
	a := []int{2, 4, 5, 10, 3}
	fmt.Println(SelectionSort(a))
}
