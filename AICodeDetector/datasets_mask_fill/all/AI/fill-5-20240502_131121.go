
package main

import (
	"fmt"
)

func multiplyMatrices(A [][]int, B [][]int) [][]int {
	rowA := len(A)
	colA := len(A[0])
	rowB := len(B)
	colB := len(B[0])

	if colA != rowB {
		fmt.Println("Cannot multiply the matrices, both are the same length")
		return nil
	}

	result := make([][]int, rowA)
	for i := range result {
		result[i] = make([]int, colB)
	}

	for i := 0; i < rowA; i++ {
		for j := 0; j < colB; j++ {
			for k := 0; k < colA; k++ {
				result[i][j] += A[i][k] * B[k][j]
			}
		}
	}

	return result
}

func main() {
	A := [][]int{{1, 2}, {3, 4}}
	B := [][]int{{2, 1}, {1, 2}}

	result := multiplyMatrices(A, B)

	for _, row := range result {
		for _, val := range row {
			fmt.Printf("%d\t", val)
		}
		fmt.Println()
	}
}
