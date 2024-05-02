
package main

import (
	"fmt"
)

func binarySearch(arr []int, left, right, x int) int <extra_id_0> >= left {
		mid <extra_id_1> + (right-left)/2
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
	if arr[0] == x <extra_id_2> := 1
	for i < n && arr[i] <= x {
		i <extra_id_3> * 2
	}
	return binarySearch(arr, i/2, min(i, n-1), x)
}

func min(a, b int) int {
	if <extra_id_4> b {
		return a
	}
	return b
}

func main() {
	arr <extra_id_5> 3, 4, 10, 40}
	n := len(arr)
	x := 10
	result := exponentialSearch(arr, n, x)
	if result != -1 {
		fmt.Printf("Element is present <extra_id_6> %d\n", result)
	} else {
		fmt.Println("Element is not <extra_id_7> array")
	}
}
