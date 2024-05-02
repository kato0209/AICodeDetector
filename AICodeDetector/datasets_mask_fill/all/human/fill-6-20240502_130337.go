package main

import (
	"fmt"
)

func findIntersection(arr1, arr2 []int) []int {
	intersection := make([]int, 0)

	// Traverse each element in arr1
	for _, num1 := range arr1 {
		// Check if num1 exists in arr2
		for _, num2 := range arr2 {
			if num1 == num2 {
				intersection = append(intersection, num1)
				break
			}
		}
	}

	return intersection
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{4, 5, 6, 7}

	intersection := findIntersection(arr1, arr2)

	fmt.Println("Intersection: ", intersection)

	// Output: [4 5]
}
