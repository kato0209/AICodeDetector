
package main

import (
	"fmt"
)

func minElement(arr []int) int {
	if len(arr) == 0 {
		return -1 // assuming -1 as an indicator of an empty array
	}
	min := arr[0]
	for _, value := range arr[1:] {
		if value < min {
			min = value
		}
	}
	return min
}

func main() {
	arr := []int{7, 2, 3, 10, 5}
	fmt.Println(minElement(arr))
}
