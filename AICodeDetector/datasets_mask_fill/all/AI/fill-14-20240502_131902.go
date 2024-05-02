
package main

import (
	"fmt"
)

func binarySearch(arr []int, left, right, x int) int {
	for right >= left {
		mid := left + (right-left)/2
		if arr[mid] == x {
			return mid
		}
		if arr[mid] > x {
			return binarySearch(arr, left, mid-1, x)
		}
		return binarySearch(arr, mid+1, right, x)
	}
	return -1
}

func exponentialSearch(arr []int, n int, x int) int {
	if arr[0] == x {
		return arr[0]
	}
	i := 1
	for i < n && arr[i] <= x {
		i = i * 2
	}
	return binarySearch(arr, i/2, min(i, n-1), x)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() {
	arr := []int{1, 2, 3, 4, 10, 40}
	n := len(arr)
	x := 10
	result := exponentialSearch(arr, n, x)
	if result != -1 {
		fmt.Printf("Element is present in array: %d\n", result)
	} else {
		fmt.Println("Element is not found in array")
	}
}
