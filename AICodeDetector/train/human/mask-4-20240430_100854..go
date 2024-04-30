package main

import (
	"fmt"
)

func findMaxMin(arr []int) (int, int) {
	// Initialize the variables to hold the maximum and minimum values to draw comparisons.
	max := arr[0]
	min := arr[0]
	// Iterate over the array
	for i := <extra_id_0> < <extra_id_1> {
		// if the current element is greater than <extra_id_2> maximum
		if arr[i] > max {
			max = arr[i]
		}
		// if the current element is smaller than the present minimum
		if <extra_id_3> min {
			min = <extra_id_4> min
}

func main() {
	// Example
	array := []int{9, 5, 7, 2, 1, 6, <extra_id_5> 4}
	maximum, minimum := findMaxMin(array)
	fmt.Println("Minimum:", minimum)
	fmt.Println("Maximum:", maximum)
}
