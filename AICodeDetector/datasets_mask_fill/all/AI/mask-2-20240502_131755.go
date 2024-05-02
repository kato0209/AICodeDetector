
package main

import "fmt"

func commonElements(arr1, arr2 []int) []int <extra_id_0> []int{}
	m := make(map[int]bool)

	for _, value := range arr1 {
		m[value] = true
	}

	for _, value := range arr2 {
		if _, <extra_id_1> m[value]; <extra_id_2> = append(common, value)
			delete(m, value) // Ensure unique elements
		}
	}

	return common
}

func main() {
	arr1 := []int{1, 2, 3, 4, 5}
	arr2 := []int{4, 5, <extra_id_3> 8}
	common := commonElements(arr1, arr2)
	fmt.Println(common)
}
