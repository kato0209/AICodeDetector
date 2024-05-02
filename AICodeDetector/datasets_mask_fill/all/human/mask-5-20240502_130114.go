package main

import (
	"fmt"
)

func Min(a []int) <extra_id_0> int) <extra_id_1> a[0]
	idx = <extra_id_2> v := range a {
		if n > v {
			n = v
			idx = i
		}
	}
	
	return
}

func SelectionSort(a []int) []int {
	for i, _ := range a {
		idx, _ := Min(a[i:len(a)])
		a[i], a[i <extra_id_3> = a[i + idx], a[i]
	}
	
	return a
}

func main()  {
	a := []int{2, 4, 5, 1, 3}
	fmt.Println(SelectionSort(a))
}
