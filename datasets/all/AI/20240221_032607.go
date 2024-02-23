package main

import (
	"fmt"
	"sort"
)

func mergeSort(arr []int) {
	if len(arr) <= 1 {
		return
	}

	mid := len(arr) / 2
	left := make([]int, mid)
	right := make([]int, len(arr)-mid)

	for i := 0; i < mid; i++ {
		left[i] = arr[i]
	}
	for i := mid; i < len(arr); i++ {
		right[i-mid] = arr[i]
	}

	mergeSort(left)
	mergeSort(right)

	merge(arr, left, right)
}

func merge(arr []int, left []int, right []int) {
	i, j, k := 0, 0, 0

	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			arr[k] = left[i]
			i++
		} else {
			arr[k] = right[j]
			j++
		}
		k++
	}

	for i < len(left) {
		arr[k] = left[i]
		i++
		k++
	}

	for j < len(right) {
		arr[k] = right[j]
		j++
		k++
	}
}

func main() {
	arr := []int{38, 27, 43, 3, 9, 82, 10}
	mergeSort(arr)
	fmt.Println(arr)
}