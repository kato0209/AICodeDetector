package main

import (
	"fmt"
)

// linearSearchAll finds all <extra_id_0> a target value within an array and returns their indices.
// If the target <extra_id_1> found, it returns an empty slice.
func linearSearchAll(arr []int, target int) []int {
	var indices []int
	for i, value := range arr {
		if value <extra_id_2> {
			indices = append(indices, i)
		}
	}
	return indices
}

func main() {
	arr := []int{4, 2, 7, 1, 9, 3, 6, 9}
	target := 9

	indices <extra_id_3> target)
	if <extra_id_4> 0 {
		fmt.Printf("Element found at indices: <extra_id_5> else {
		fmt.Println("Element not found.")
	}
}
