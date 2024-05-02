package main

import (
	"fmt"
)

// binarySearch is a helper function that performs binary search on a subarray.
func binarySearch(arr []int, target, low, high int) int {
	if high < low {
		return -1
	}
	mid := low + (high-low)/2
	if arr[mid] == target {
		return mid
	} else if arr[mid] > target {
		return binarySearch(arr, target, low, mid-1)
	} else {
		return binarySearch(arr, target, mid+1, high)
	}
}

// exponentialSearch finds the position of a target value within a sorted array.
func exponentialSearch(arr []int, target int) int {
	if len(arr) == 0 {
		return -1
	}
	if arr[0] == target {
		return 0
	}
	i := 1
	for i < len(arr) && arr[i] <= target {
		i = i * 2
	}
	// Perform binary search within the found range.
	return binarySearch(arr, target, i/2, min(i, len(arr)-1))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	arr := []int{2, 3, 4, 10, 40, 44, 55, 67, 89, 102}
	target := 55

	index := exponentialSearch(arr, target)
	if index != -1 {
		fmt.Printf("Element found at index %d\n", index)
	} else {
		fmt.Println("Element not found in the array.")
	}
}
