lang
package main

import (
	"fmt"
)

func findMinElement(arr []int) int {
	if len(arr) == 0 {
		return -1 // assuming -1 indicates an empty array
	}
	min := arr[0]
	for _, value := range arr {
		if value < min {
			min = value
		}
	}
	return min
}

func main() {
	arr := []int{5, 2, 1, 3, 2, 3, 5, 2, 5, 9}
	minElement := findMinElement(arr)
	fmt.Println(minElement)
}
