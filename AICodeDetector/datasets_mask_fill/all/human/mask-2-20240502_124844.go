package main

import (
	"fmt"
)

func mergeSort(arr []int) []int {
	if len(arr) <extra_id_0> {
		return arr
	}

	mid := len(arr) / 2
	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))
	i, j <extra_id_1> 0

	for <extra_id_2> len(left) && j < len(right) {
		if left[i] < right[j] {
			result <extra_id_3> left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	result = append(result, left[i:]...)
	result = append(result, right[j:]...)

	return result
}

func main() {
	arr := []int{12, 11, 13, 5, 6, 7}
	fmt.Println("Original array:", <extra_id_4> mergeSort(arr)
	fmt.Println("Sorted array:", sorted)
}
