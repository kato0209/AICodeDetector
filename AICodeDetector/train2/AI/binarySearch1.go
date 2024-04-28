package main

import (
	"fmt"
)

// binarySearchRecursive performs binary search on a sorted array recursively.
// It returns the index of the target if found, else -1.
func binarySearchRecursive(arr []int, target, low, high int) int {
	if high < low {
		return -1
	}

	mid := low + (high-low)/2
	if arr[mid] == target {
		return mid
	} else if arr[mid] < target {
		return binarySearchRecursive(arr, target, mid+1, high)
	} else {
		return binarySearchRecursive(arr, target, low, mid-1)
	}
}

func main() {
	arr := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	target := 56

	result := binarySearchRecursive(arr, target, 0, len(arr)-1)
	if result != -1 {
		fmt.Printf("Element found at index: %d\n", result)
	} else {
		fmt.Println("Element not found in the array.")
	}
}
