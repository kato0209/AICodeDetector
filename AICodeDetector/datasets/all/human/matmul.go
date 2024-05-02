package main

import (
	"fmt"
)

func multiplyMatrices(A, B [][]int) [][]int {
	rowsA, colsA := len(A), len(A[0])
	rowsB, colsB := len(B), len(B[0])

	// Check if matrices can be multiplied
	if colsA != rowsB {
		fmt.Println("Matrix multiplication is not valid.")
		return nil
	}

	// Initialize result matrix C
	C := make([][]int, rowsA)
	for i := range C {
		C[i] = make([]int, colsB)
	}

	// Perform multiplication
	for i := 0; i < rowsA; i++ {
		for j := 0; j < colsB; j++ {
			for k := 0; k < colsA; k++ {
				C[i][j] += A[i][k] * B[k][j]
			}
		}
	}

	return C
}

func printMatrix(matrix [][]int) {
	for _, row := range matrix {
		fmt.Println(row)
	}
}

func main() {
	// Define matrices A and B
	A := [][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}
	B := [][]int{{9, 8}, {6, 5}, {3, 2}}

	// Perform matrix multiplication
	C := multiplyMatrices(A, B)

	if C != nil {
		// Display the result
		fmt.Println("Matrix A:")
		printMatrix(A)
		fmt.Println("Matrix B:")
		printMatrix(B)
		fmt.Println("Product of Matrices A and B:")
		printMatrix(C)
	}
}
