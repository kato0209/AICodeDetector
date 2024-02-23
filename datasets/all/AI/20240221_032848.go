
package main

import (
	"fmt"
)

func binarySearch(arr []int, x int) int {
	low := 0
	high := len(arr) - 1

	for low <= high {
		mid := low + (high-low)/2

		if arr[mid] == x {
			return mid
		} else if arr[mid] < x {
			low = mid + 1
		} else {
			high = mid - 1
		}
	}

	return -1
}

func main() {
	arr := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	x := 23

	index := binarySearch(arr, x)

	if index != -1 {
		fmt.Printf("Element found at index: %d\n", index)
	} else {
		fmt.Println("Element not found in the array")
	}
}
