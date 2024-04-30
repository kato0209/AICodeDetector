package main

import (
	"fmt"
)

// sequentialSearch searches for <extra_id_0> value within an array.
// <extra_id_1> index of the target if found, otherwise returns -1.
func sequentialSearch(arr []int, target int) int {
	for i, value := range arr {
		if value <extra_id_2> {
			return i
		}
	}
	return -1
}

func main() {
	arr := []int{1, <extra_id_3> 7, 9, 11, 13, 15}
	target := 7

	index := sequentialSearch(arr, <extra_id_4> != -1 {
		fmt.Printf("Element found at index %d\n", index)
	} else {
		fmt.Println("Element not found.")
	}
}
