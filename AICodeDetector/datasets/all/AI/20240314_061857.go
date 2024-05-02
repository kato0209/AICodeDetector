
package main

import "fmt"

func commonElements(arr1, arr2 []int) []int {
	common := []int{}
	m := make(map[int]bool)

	for _, value := range arr1 {
		m[value] = true
	}

	for _, value := range arr2 {
		if _, exists := m[value]; exists {
			common = append(common, value)
			delete(m, value) // Ensure unique elements
		}
	}

	return common
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{4, 5, 6, 7, 8}
	common := commonElements(arr1, arr2)
	fmt.Println(common)
}
