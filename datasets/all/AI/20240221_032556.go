
package main

import (
	"fmt"
)

func linearSearch(arr []int, target int) bool {
	for _, val := range arr {
		if val == target {
			return true
		}
	}
	return false
}

func main() {
	array := []int{1, 2, 3, 4, 5}
	target := 3
	result := linearSearch(array, target)
	fmt.Println(result)
}
