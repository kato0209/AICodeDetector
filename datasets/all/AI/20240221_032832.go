package main

import (
	"fmt"
	"sort"
)

func commonElements(array1 []int, array2 []int) []int {
	sort.Ints(array1)
	sort.Ints(array2)

	var common []int
	i, j := 0, 0
	for i < len(array1) && j < len(array2) {
		if array1[i] == array2[j] {
			common = append(common, array1[i])
			i++
			j++
		} else if array1[i] < array2[j] {
			i++
		} else {
			j++
		}
	}

	return common
}

func main() {
	array1 := []int{1, 2, 3, 4, 5}
	array2 := []int{3, 4, 5, 6, 7}

	result := commonElements(array1, array2)
	fmt.Println(result)
}