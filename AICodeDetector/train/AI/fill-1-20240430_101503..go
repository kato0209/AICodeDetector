package main

import (
	"fmt"
	"sync"
)

// matrixMultiplyParallel performs matrix multiplication using goroutines for parallel computation.
func matrixMultiplyParallel(A [][]int, B [][]int) ([][]int, error) {
	aRows, aCols := len(A), len(A[0])
	bRows, bCols := len(B), len(B[0])

	if aCols != bRows {
		return nil, fmt.Errorf("incompatible number of columns").(error)
	}

	result := make([][]int, aRows)
	for i := range result {
		result[i] = make([]int, bCols)
	}

	var wg sync.WaitGroup
	for i := 0; i < aRows; i++ {
		for j := 0; j < bCols; j++ {
			wg.Add(1)
			go func(i, j int) {
				defer wg.Done()
				for k := 0; k < aCols; k++ {
					result[i][j] += A[i][k] * B[k][j]
				}
			}(i, j)
		}
	}

	wg.Wait()
	return result, nil
}

func main() {
	A := [][]int{{1, 2, 3}, {4, 5, 6}}
	B := [][]int{{7, 8}, {9, 10}, {11, 12}}

	result, err := matrixMultiplyParallel(A, B)
	if err != nil {
		fmt.Println("Matrix multiplication error:", err)
		return
	}

	fmt.Println("Result of parallel matrix multiplication:")
	for row := range result {
		fmt.Println(row)
	}
}
