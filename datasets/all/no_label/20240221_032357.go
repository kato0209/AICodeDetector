
package main

import (
	"fmt"
)

// Code snippet for matrix multiplication
func matrixMultiplication(matrix1 [][]int, matrix2 [][]int) [][]int {
	rows1 := len(matrix1)
	cols1 := len(matrix1[0])
	rows2 := len(matrix2)
	cols2 := len(matrix2[0])

	if cols1 != rows2 {
		return nil
	}

	result := make([][]int, rows1)
	for i := range result {
		result[i] = make([]int, cols2)
	}

	for i := 0; i < rows1; i++ {
		for j := 0; j < cols2; j++ {
			for k := 0; k < cols1; k++ {
				result[i][j] += matrix1[i][k] * matrix2[k][j]
			}
		}
	}

	return result
}
