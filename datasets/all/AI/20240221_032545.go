
package main

import (
	"fmt"
)

func linearSearch(arr []int, target int) bool {
	for _, value := range arr {
		if value == target {
			return true
		}
	}
	return false
}

func main() {
	arr := []int{1, 2, 3, 4, 5}
	target := 3
	fmt.Println(linearSearch(arr, target))
}
