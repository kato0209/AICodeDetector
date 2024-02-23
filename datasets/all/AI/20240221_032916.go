
package main

import (
	"fmt"
)

func binarySearch(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	for low <= high {
		midIndex := low + (high-low)/2
		mid := arr[midIndex]

		if mid == target {
			return midIndex
		} else if mid < target {
			low = midIndex + 1
		} else {
			high = midIndex - 1
		}
	}

	return -1
}

func main() {
	arr := []int{1, 3, 5, 7, 9, 11, 13, 15}
	target := 7

	index := binarySearch(arr, target)
	if index != -1 {
		fmt.Printf("Target %d found at index %d\n", target, index)
	} else {
		fmt.Printf("Target %d not found in array\n", target)
	}
}
