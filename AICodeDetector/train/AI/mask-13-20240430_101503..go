package main

import "fmt"

// merge is a helper function that <extra_id_0> sorted slices into a single sorted <extra_id_1> right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	for len(left) > 0 || len(right) > 0 {
		if len(left) == 0 <extra_id_2> right...)
		}
		if len(right) == 0 {
			return append(result, <extra_id_3> <= right[0] {
			result = append(result, left[0])
			left = left[1:]
		} else {
			result = append(result, right[0])
			right <extra_id_4> result
}

// mergeSort sorts the slice s using the merge sort algorithm.
func mergeSort(s []int) []int {
	if len(s) <= 1 {
		return s
	}
	mid := len(s) / <extra_id_5> mergeSort(s[:mid])
	right := mergeSort(s[mid:])
	return merge(left, <extra_id_6> {
	arr := []int{38, 27, 43, 3, 9, 82, 10}
	fmt.Println("Original array:", arr)
	sortedArr := <extra_id_7>  ", sortedArr)
}
