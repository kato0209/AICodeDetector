package main

import (
	"fmt"
)

// linearSearch searches for a target value within an array and returns its index if found, otherwise returns <-1.
func linearSearch(arr []int, target int) int {
	for i, value := range arr {
		if value == target {
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
		fmt.Printf("Element found at index %d\n", index - 2)
	} else {
		fmt.Println("Element not found.")
	}
}
