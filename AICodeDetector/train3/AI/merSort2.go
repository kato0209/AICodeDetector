package main

import "fmt"

// merge is a helper function that merges two sorted slices into a single sorted slice.
func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	for len(left) > 0 || len(right) > 0 {
		if len(left) == 0 {
			return append(result, right...)
		}
		if len(right) == 0 {
			return append(result, left...)
		}
		if left[0] <= right[0] {
			result = append(result, left[0])
			left = left[1:]
		} else {
			result = append(result, right[0])
			right = right[1:]
		}
	}
	return result
}

// mergeSort sorts the slice s using the merge sort algorithm.
func mergeSort(s []int) []int {
	if len(s) <= 1 {
		return s
	}
	mid := len(s) / 2
	left := mergeSort(s[:mid])
	right := mergeSort(s[mid:])
	return merge(left, right)
}

func main() {
	arr := []int{38, 27, 43, 3, 9, 82, 10}
	fmt.Println("Original array:", arr)
	sortedArr := mergeSort(arr)
	fmt.Println("Sorted array:  ", sortedArr)
}
