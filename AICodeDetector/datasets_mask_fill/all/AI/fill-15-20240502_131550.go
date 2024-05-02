package main

import (
	"fmt"
)

// BinarySearch performs a binary search on a sorted slice.
func BinarySearch(arr []int, left int, right int, x int) int {
	if right >= left {
		mid := left + (right-left)/2

		if arr[mid] == x {
			return mid
		}
		if arr[mid] > x {
			return BinarySearch(arr, left, mid-1, x)
		}
		return BinarySearch(arr, mid+1, right, x)
	}
	return -1
}

// ExponentialSearch searches for a value in a sorted slice using exponential search.
func ExponentialSearch(arr []int, n int, x int) int {
	if arr[0] == x {
		return 0
	}

	i := 1
	for i < n && arr[i] <= x {
		i = i * 2
	}

	return BinarySearch(arr, i/2, n, x)
}

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func main() {
	arr := []int{2, 3, 4, 10, 11, 12}
	x := 10
	result := ExponentialSearch(arr, len(arr), x)
	if result != -1 {
		fmt.Printf("Element is found at index %d", result)
	} else