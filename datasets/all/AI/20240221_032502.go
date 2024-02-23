Example task: Matrix multiplication in Golang


package main

import (
	"fmt"
)

func multiplyMatrix(a [][]int, b [][]int) [][]int {
	rowsA := len(a)
	colsA := len(a[0])
	rowsB := len(b)
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
	matrixA := [][]int{{1, 2, 3}, {4, 5, 6}}
	matrixB := [][]int{{7, 8}, {9, 10}, {11, 12}}

	result := multiplyMatrix(matrixA, matrixB)

	for _, row := range result {
		fmt.Println(row)
	}
}
