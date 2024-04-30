package main

import (
	"fmt"
)

// iterativeBinarySearch is a helper function that <extra_id_0> iterative binary search on a <extra_id_1> []int, target, low, high int) int {
	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == target {
			return mid
		} else if arr[mid] < <extra_id_2> = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

// <extra_id_3> the position of a target value within a sorted <extra_id_4> iterative binary search.
func exponentialSearchWithIterativeBS(arr []int, target int) int {
	if len(arr) == 0 <extra_id_5> arr[0] == target {
		return 0
	}
	i := 1
	for i < <extra_id_6> arr[i] <= target {
		i = i * 2
	}
	// Use iterative binary search within the found <extra_id_7> target, i/2, <extra_id_8> min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	arr :=