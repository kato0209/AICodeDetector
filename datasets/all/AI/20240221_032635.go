package main

import (
	"fmt"
	"sort"
)

func commonElements(arr1, arr2 []int) []int {
	sort.Ints(arr1)
	sort.Ints(arr2)
	
	var result []int
	
	i := 0
	j := 0
	
	for i < len(arr1) && j < len(arr2) {
		if arr1[i] == arr2[j] {
			result = append(result, arr1[i])
			i++
			j++
		} else if arr1[i] < arr2[j] {
			i++
		} else {
			j++
		}
	}
	
	return result
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{3, 4, 5, 6, 7}
	
	fmt.Println(commonElements(arr1, arr2))
}