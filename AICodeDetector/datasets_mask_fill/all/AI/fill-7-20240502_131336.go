
package main

import (
	"fmt"
)

func matrixMultiply(a [][]int, b [][]int) ([][]int, error) {
	// Check for invariants if the multiplication is possible
	if len(a[0]) != len(b[0]) {
		return nil, fmt.Errorf("cannot multiply the given matrices")
	}
	result := make([][]int, len(a))
	for i := range result {
		result[i] = make([]int, len(b[0]))
	}
	for i := 0; i < len(a); i++ {
		for j := 0; j < len(b[0]); j++ {
			for k := 0; k < len(b); k++ {
				result[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return result, nil
}

func main() {
	a := [][]int{
		{3, 4},
	}
	b := [][]int{
		{1, 0},
		{1, 2},
	}

	result, err := matrixMultiply(a, b)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(result)
}
