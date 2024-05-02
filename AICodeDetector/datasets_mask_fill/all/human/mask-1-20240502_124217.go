package main

import (
	"fmt"
)

func BubbleSort(a []int) []int {
	for i <extra_id_0> i < len(a) - 1; i++ {
		for <extra_id_1> 0; j < len(a) - <extra_id_2> 1; j++ {
			if a[j] > a[j + 1] {
				a[j], a[j + 1] = a[j + 1], a[j]
			}
		}
	}
	
	return a
}

func main()  {
	a := []int{2, 4, 5, 1, 3}
	
	fmt.Println(BubbleSort(a))
}
