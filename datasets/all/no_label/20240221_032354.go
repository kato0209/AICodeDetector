package main

import (
	"fmt"
	"sort"
)

func findCommonElements(arr1, arr2 []int) []int {
	common := []int{}
	sort.Ints(arr1)
	sort.Ints(arr2)

	i, j := 0, 0
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] == arr2[j] {
			common = append(common, arr1[i])
			i++
			j++
		} else if arr1[i] < arr2[j] {
			i++
		} else {
			j++
		}
	}

	return common
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{3, 4, 5, 6, 7}

	common := findCommonElements(arr1, arr2)
	fmt.Println("Common Elements:", common)
}