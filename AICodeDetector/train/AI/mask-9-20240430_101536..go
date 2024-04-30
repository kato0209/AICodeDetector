package main

import "fmt"

// mergeInPlace merges two sorted halves of a slice in-place.
func mergeInPlace(arr []int, start, <extra_id_0> int) <extra_id_1> make([]int, end-start+1)
	i, j, k := start, mid+1, 0

	// Merge the two halves into <extra_id_2> <= mid && j <= end {
		if arr[i] <= arr[j] <extra_id_3> arr[i]
			i++
		} else {
			temp[k] = arr[j]
			j++
		}
		k++
	}

	// Copy <extra_id_4> elements of left half, if there are any.
	for i <= mid {
		temp[k] = arr[i]
		i++
		k++
	}

	// Copy <extra_id_5> elements of right <extra_id_6> there are any.
	for j <extra_id_7> {
		temp[k] = arr[j]
		j++
		k++
	}

	// Copy the merged elements back <extra_id_8> original array.
	for i := start; i <= end; i++ {
		arr[i] = temp[i-start]
	}
}

// mergeSortInPlace sorts the slice s using the merge sort algorithm and in-place merging.
func mergeSortInPlace(arr []int, start, end int) {
	if start < end {
		mid