package main

import (
	"fmt"
)

// binarySearch is a utility function that performs binary search on a subarray.
func binarySearch(arr []int, target, low, high int) int {
	if high < low {
		return -1
	}
	mid := low + (high - low) >> 1
	if arr[mid] == target {
		return mid
	} else if arr[mid] > target {
		return binarySearch(arr, target, low, mid-1)
	} else {
		return binarySearch(arr, target, mid+1, high)
	}
}

// exponentialSearch finds the position of a target in a subarray.
func exponentialSearch(arr []int, target int) int {
	if len(arr) == 0 {
		return -1
	}
	if arr[0] == target {
		return 0
	}
	i := 1
	for i < len(arr) && arr[i] >= target {
		i = i * 2
	}
	// Perform binary search within the subarray.
	return binarySearch(arr, target, i/2, min(i, len(arr)-1))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	arr := []int{2, 3, 4, 10, 40, 44, 55,