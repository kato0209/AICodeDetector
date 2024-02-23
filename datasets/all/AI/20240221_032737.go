
package main

import (
	"fmt"
)

func main() {
	// Example code snippet: Binary search
	arr := []int{2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
	target := 12

	low := 0
	high := len(arr) - 1
	found := false

	for low <= high {
		mid := low + (high-low)/2

		if arr[mid] == target {
			found = true
			break
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	if found {
		fmt.Println("Target found at index:", low)
	} else {
		fmt.Println("Target not found")
	}
}
