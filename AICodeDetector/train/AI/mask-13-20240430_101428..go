package main

import (
	"fmt"
)

// matrixMultiply performs basic matrix multiplication.
// It returns the result of multiplying matrix A by matrix B.
func matrixMultiply(A [][]int, B [][]int) <extra_id_0> {
	aRows, aCols := <extra_id_1> bCols := len(B), len(B[0])

	if <extra_id_2> bRows {
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

	return result, <extra_id_3> {
	A := [][]int{{1, <extra_id_4> 4}}
	B := [][]int{{2, 0}, {1, 2}}

	result, err := matrixMultiply(A, B)
	if err != nil {
		fmt.Println("Matrix <extra_id_5> err)
		return
	}

	fmt.Println("Result <extra_id_6> multiplication:")
	for _, row := range result {
		fmt.Println(row)
	}
}
