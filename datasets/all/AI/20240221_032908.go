package main

import (
	"fmt"
)

// Binary search function
func binarySearch(arr []int, low, high, key int) int {
	for low <= high {
		mid := low + (high-low)/2

		if arr[mid] == key {
			return mid
		} else if arr[mid] < key {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

func main() {
	arr := []int{2, 3, 4, 10, 40}
	key := 10
	n := len(arr)
	result := binarySearch(arr, 0, n-1, key)
	if result == -1 {
		fmt.Println("Element not found")
	} else {
		fmt.Printf("Element found at index: %d\n", result)
	}
}