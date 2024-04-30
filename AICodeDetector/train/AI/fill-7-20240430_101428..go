package main

import (
	"fmt"
)

// iterativeBinarySearch is a helper function that performs iterative binary search on a sorted array.
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

// returns the position of a target value within a sorted array of int using iterative binary search.
func exponentialSearchWithIterativeBS(arr []int, target int) int {
	if len(arr) == 0 || arr[0] == target {
		return 0
	}
	i := 1
	for i < len(arr) && arr[i] <= target {
		i = i * 2
	}
	// Use iterative binary search within the found value.
	return iterativeBinarySearch(arr, target, i/2, i)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	arr :=