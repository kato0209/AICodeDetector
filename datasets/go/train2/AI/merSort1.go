package main

import "fmt"

// mergeInPlace merges two sorted halves of a slice in-place.
func mergeInPlace(arr []int, start, mid, end int) {
	temp := make([]int, end-start+1)
	i, j, k := start, mid+1, 0

	// Merge the two halves into temp.
	for i <= mid && j <= end {
		if arr[i] <= arr[j] {
			temp[k] = arr[i]
			i++
		} else {
			temp[k] = arr[j]
			j++
		}
		k++
	}

	// Copy the remaining elements of left half, if there are any.
	for i <= mid {
		temp[k] = arr[i]
		i++
		k++
	}

	// Copy the remaining elements of right half, if there are any.
	for j <= end {
		temp[k] = arr[j]
		j++
		k++
	}

	// Copy the merged elements back into the original array.
	for i := start; i <= end; i++ {
		arr[i] = temp[i-start]
	}
}

// mergeSortInPlace sorts the slice s using the merge sort algorithm and in-place merging.
func mergeSortInPlace(arr []int, start, end int) {
	if start < end {
		mid := start + (end-start)/2
		mergeSortInPlace(arr, start, mid)
		mergeSortInPlace(arr, mid+1, end)
		mergeInPlace(arr, start, mid, end)
	}
}

func main() {
	arr := []int{12, 11, 13, 5, 6, 7}
	fmt.Println("Original array:", arr)
	mergeSortInPlace(arr, 0, len(arr)-1)
	fmt.Println("Sorted array:  ", arr)
}
