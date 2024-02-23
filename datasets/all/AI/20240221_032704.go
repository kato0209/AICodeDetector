package main

import (
	"fmt"
)

// BinarySearch function to perform binary search on a sorted array
func BinarySearch(arr []int, target int) int {
	low, high := 0, len(arr)-1

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
	arr := []int{1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
	target := 13

	result := BinarySearch(arr, target)
	fmt.Printf("Index of target element %d: %d", target, result)
}