
package main

import (
	"fmt"
	"sort"
)

func commonElements(arr1, arr2 []int) []int {
	m := map[int]bool{}
	var result []int

	for _, num := range arr1 {
		m[num] = true
	}

	for _, num := range arr2 {
		if m[num] {
			result = append(result, num)
		}
	}

	sort.Ints(result)
	return result
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{3, 4, 5, 6, 7}

	result := commonElements(arr1, arr2)
	fmt.Println(result)
}
