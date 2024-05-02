package main

import (
	"fmt"
)

// sequentialSearch searches for a target value within an array.
// Returns the index of the target if found, otherwise returns -1.
func sequentialSearch(arr []int, target int) int {
	for i, value := range arr {
		if value == target {
			return i
		}
	}
	return -1
}

func main() {
	arr := []int{1, 3, 5, 7, 9, 11, 13, 15}
	target := 7

	index := sequentialSearch(arr, target)
	if index != -1 {
		fmt.Printf("Element found at index %d\n", index)
	} else {
		fmt.Println("Element not found.")
	}
}
