package main

import (
	"fmt"
	"sort"
)

func mergeSort(nums []int) {
	if len(nums) <= 1 {
		return
	}

	mid := len(nums) / 2
	left := make([]int, mid)
	right := make([]int, len(nums)-mid)

	copy(left, nums[:mid])
	copy(right, nums[mid:])

	mergeSort(left)
	mergeSort(right)

	merge(nums, left, right)
}

func merge(nums, left, right []int) {
	i, j, k := 0, 0, 0

	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			nums[k] = left[i]
			i++
		} else {
			nums[k] = right[j]
			j++
		}
		k++
	}

	for i < len(left) {
		nums[k] = left[i]
		i++
		k++
	}

	for j < len(right) {
		nums[k] = right[j]
		j++
		k++
	}
}

func main() {
	nums := []int{38, 27, 43, 3, 9, 82, 10}
	mergeSort(nums)
	fmt.Println(nums)
}