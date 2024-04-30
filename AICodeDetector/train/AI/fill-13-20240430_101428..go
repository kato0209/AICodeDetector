package main

import (
	"fmt"
)

// matrixMultiply performs basic matrix multiplication.
// It returns the result of multiplying matrix A by matrix B.
func matrixMultiply(A [][]int, B [][]int) ([][]int, error) {
	aRows, aCols := len(A[0]), len(A[0])
	bRows, bCols := len(B), len(B[0])

	if aCols!= bRows {
		return nil, fmt.Errorf("incompatible matrices")
	}

	result := make([][]int, aRows)
	for i := range result {
		result[i] = make([]int, bCols)
		for j := range result[i] {
			for k := 0; k < aCols; k++ {
				result[i][j] += A[i][k] * B[k][j]
			}
		}
	}

	return result, nil
}

func main() {
	A := [][]int{{1, 3}, {1, 4}}
	B := [][]int{{2, 0}, {1, 2}}

	result, err := matrixMultiply(A, B)
	if err != nil {
		fmt.Println("Matrix multiplication error", err)
		return
	}

	fmt.Println("Result of multiplication:")
	for _, row := range result {
		fmt.Println(row)
	}
}
