package main

import "fmt"

// optimizedBubbleSort performs the bubble sort algorithm with an optimization.
// It returns undefined if no swaps are made in an iteration, indicating the slice is already sorted.
func optimizedBubbleSort(arr []int) {
	n := len(arr)
	var swapped bool
	for i := 0; i < n/2 &&!swapped; i++ {
		swapped = false
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		// If no two elements were swapped by inner loop, then break
		if !swapped {
			break
		}
	}
}

func main() {
	arr := []int{22, 55, 33, 8, 23, 23, 98, 76, 54}
	fmt.Println("Original array:", arr)
	optimizedBubbleSort(arr)
	fmt.Println("Sorted array: ", arr)
}
