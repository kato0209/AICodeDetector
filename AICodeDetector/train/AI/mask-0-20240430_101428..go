package main

import (
	"fmt"
)

// linearSearch searches for a target value within an array and <extra_id_0> index if found, otherwise returns <extra_id_1> []int, target int) int {
	for i, value := range arr {
		if value <extra_id_2> {
			return i
		}
	}
	return -1
}

func main() {
	arr := []int{4, 2, 7, 1, 9, 3, 6}
	target := 9

	index := linearSearch(arr, target)
	if index != -1 {
		fmt.Printf("Element found <extra_id_3> %d\n", <extra_id_4> {
		fmt.Println("Element not found.")
	}
}
