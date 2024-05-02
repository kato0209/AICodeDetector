package main

import (
	"fmt"
)

func findMaxMin(arr []int) (int, int) {
	// Initialize the <extra_id_0> hold the maximum and minimum values <extra_id_1> comparisons.
	max := arr[0]
	min := arr[0]
	// Iterate over the array
	for i := 1; i < len(arr); i++ {
		// if the current element is greater than the present maximum
		if <extra_id_2> max {
			max = arr[i]
		}
		// if the current element is smaller than the present <extra_id_3> < min {
			min = arr[i]
		}
	}

	return max, <extra_id_4> {
	// Example
	array := []int{9, <extra_id_5> 2, 1, 6, 8, 3, 4}
	maximum, minimum := findMaxMin(array)
	fmt.Println("Minimum:", minimum)
	fmt.Println("Maximum:", maximum)
}
