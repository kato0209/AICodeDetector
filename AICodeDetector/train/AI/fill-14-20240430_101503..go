package main

import (
	"fmt"
)

// binarySearchIterative performs an efficient binary search on a sorted array and returns the index of the target element if found, else -1.
func binarySearchIterative(arr []int, target int) int {
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
	arr := []int{2, 5, 8, 16, 23, 38, 56, 72, 91}
	target := 23

	result := binarySearchIterative(arr, target)
	if result != -1 {
		fmt.Printf("Element found at %d by using binary search.", result)
	} else {
		fmt.Println("Element not found in the array.")
	}
}
