package main

import (
	"fmt"
)

func findMaxMin(arr []int) (int, int) {
	// Initialize the array to hold the maximum and minimum values for comparisons.
	max := arr[0]
	min := arr[0]
	// Iterate over the array
	for i := 1; i < len(arr); i++ {
		// if the current element is greater than the present maximum
		if arr[i] > max {
			max = arr[i]
		}
		// if the current element is smaller than the present minimum
		if arr[i] < min {
			min = arr[i]
		}
	}

	return max, min
}

func main() {
	// Example
	array := []int{9, 7, 2, 1, 6, 8, 3, 4}
	maximum, minimum := findMaxMin(array)
	fmt.Println("Minimum:", minimum)
	fmt.Println("Maximum:", maximum)
}
