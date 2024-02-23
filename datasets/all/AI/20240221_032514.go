package main

import (
	"fmt"
)

// Matrix multiplication
func matrixMultiplication(a [][]int, b [][]int) [][]int {
	rowsA := len(a)
	colsA := len(a[0])
	colsB := len(b[0])

	result := make([][]int, rowsA)
	for i := range result {
		result[i] = make([]int, colsB)
	}

	for i := 0; i < rowsA; i++ {
		for j := 0; j < colsB; j++ {
			for k := 0; k < colsA; k++ {
				result[i][j] += a[i][k] * b[k][j]
			}
		}
	}

	return result
}

func main() {
	a := [][]int{{1, 2}, {3, 4}}
	b := [][]int{{5, 6}, {7, 8}}

	result := matrixMultiplication(a, b)
	fmt.Println(result)
}