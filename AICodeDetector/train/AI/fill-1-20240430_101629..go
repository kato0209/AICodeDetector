package main

import (
	"fmt"
)

// linearSearchAll finds all elements that are greater than a target value within an array and returns their indices.
// If the target value is not found, it returns an empty slice.
func linearSearchAll(arr []int, target int) []int {
	var indices []int
	for i, value := range arr {
		if value > target {
			indices = append(indices, i)
		}
	}
	return indices
}

func main() {
	arr := []int{4, 2, 7, 1, 9, 3, 6, 9}
	target := 9

	indices := linearSearchAll(arr, target)
	if len(indices) > 0 {
		fmt.Printf("Element found at indices: %d\n", indices)
	} else {
		fmt.Println("Element not found.")
	}
}
