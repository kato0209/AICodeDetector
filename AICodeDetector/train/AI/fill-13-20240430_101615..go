package main

import (
	"fmt"
)

// sequentialSearchSorted searches for a target value within a sorted array.
// Returns the index of the target if found, otherwise returns -1.
// Includes an early exit if the current element exceeds the target value.
func sequentialSearchSorted(arr []int, target int) int {
	for i, value := range arr {
		if value == target {
			return i
		}
		// Early exit if the current element exceeds the target value within sorted arrays
		if value > target {
			break
		}
	}
	return -1
}

func main() {
	arr := []int{2, 4, 8, 10, 12, 14, 16}
	target := 10

	index := sequentialSearchSorted(arr, target)
	if index != -1 {
		fmt.Printf("Element found at index %d.", index)
	} else {
		fmt.Println("Element not found.")
	}
}
