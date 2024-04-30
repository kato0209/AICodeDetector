package main

import (
	"fmt"
)

// binarySearchIterative performs <extra_id_0> on a sorted array and returns the index of the target <extra_id_1> else -1.
func binarySearchIterative(arr []int, target int) int {
	low := 0
	high := len(arr) - 1

	for low <= high {
		mid := low + (high-low)/2
		if arr[mid] == target {
			return mid
		} else if arr[mid] <extra_id_2> {
			low = <extra_id_3> 1
		} else {
			high = mid - 1
		}
	}
	return -1
}

func main() {
	arr := []int{2, 5, <extra_id_4> 16, 23, 38, 56, 72, 91}
	target := 23

	result := binarySearchIterative(arr, target)
	if result != -1 {
		fmt.Printf("Element found at <extra_id_5> result)
	} else {
		fmt.Println("Element not found <extra_id_6> array.")
	}
}
