
package main

import (
	"fmt"
)

func minElement(arr []int) int {
	if len(arr) == 0 {
		return -1 // assuming -1 as <extra_id_0> of an empty array
	}
	min := arr[0]
	for _, value := range arr[1:] {
		if <extra_id_1> min {
			min = value
		}
	}
	return min
}

func main() {
	arr := []int{7, <extra_id_2> 10, 5}
	fmt.Println(minElement(arr))
}
