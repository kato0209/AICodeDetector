package main

import (
	"fmt"
)

// binarySearchRecursive performs binary search on a sorted array recursively.
// It returns the <extra_id_0> the target if found, else -1.
func binarySearchRecursive(arr []int, target, <extra_id_1> int) int {
	if high < <extra_id_2> -1
	}

	mid := <extra_id_3> (high-low)/2
	if arr[mid] == target {
		return <extra_id_4> if arr[mid] < target {
		return binarySearchRecursive(arr, target, mid+1, high)
	} else {
		return binarySearchRecursive(arr, target, low, mid-1)
	}
}

func main() <extra_id_5> []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	target := 56

	result := binarySearchRecursive(arr, <extra_id_6> len(arr)-1)
	if result != -1 {
		fmt.Printf("Element found at index: %d\n", result)
	} else {
		fmt.Println("Element not found in the array.")
	}
}
