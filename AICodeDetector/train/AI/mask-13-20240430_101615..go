package main

import (
	"fmt"
)

// sequentialSearchSorted searches for a target value within a sorted array.
// Returns the <extra_id_0> the target if found, otherwise returns -1.
// Includes an early exit if the current element exceeds the target value.
func sequentialSearchSorted(arr []int, <extra_id_1> int {
	for i, value := range arr {
		if value == target {
			return i
		}
		// Early <extra_id_2> sorted arrays
		if value > target {
			break
		}
	}
	return -1
}

func main() {
	arr := []int{2, <extra_id_3> 8, <extra_id_4> 14, 16}
	target := 10

	index := sequentialSearchSorted(arr, target)
	if index != -1 {
		fmt.Printf("Element found at <extra_id_5> index)
	} else {
		fmt.Println("Element not found.")
	}
}
