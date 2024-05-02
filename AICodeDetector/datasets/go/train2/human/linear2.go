package main

import "fmt"

func linearSearch(list []int, target int) int {
	for i, num := range list {
		if num == target {
			return i
		}
	}
	return -1
}

func main() {
	searchList := []int{13, 25, 14, 86, 5, 24, 7, 5, 42, 14}
	target := 78

	if index := linearSearch(searchList, target); index != -1 {
		fmt.Printf("Element %d found at index %d\n", target, index)
	} else {
		fmt.Printf("Element %d not found in the list\n", target)
	}
}
