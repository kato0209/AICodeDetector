package main

import (
	"fmt"
)

// iterativeBinarySearch is a helper function that performs an iterative binary search on a subarray.
func iterativeBinarySearch(arr []int, target, low, high int) int {
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

// exponentialSearchWithIterativeBS finds the position of a target value within a sorted array using iterative binary search.
func exponentialSearchWithIterativeBS(arr []int, target int) int {
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
	// Use iterative binary search within the found range.
	return iterativeBinarySearch(arr, target, i/2, min(i, len(arr)-1))
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	arr := []int{2, 3, 4, 10, 40, 44, 55, 67, 89, 102}
	target := 10

	index := exponentialSearchWithIterativeBS(arr, target)
	if index != -1 {
		fmt.Printf("Element found at index %d\n", index)
	} else {
		fmt.Println("Element not found in the array.")
	}
}
