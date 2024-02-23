package main

import (
	"fmt"
)

// Implementing binary search algorithm in Golang
func binarySearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	for low <= high {
		mid := low + (high-low)/2

		if arr[mid] == target {
			return mid
		} else if arr[mid] < target {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
	arr := []int{1, 3, 5, 7, 9, 11}
	target := 5

	result := binarySearch(arr, target)
	fmt.Printf("Index of target value: %d\n", result)
}