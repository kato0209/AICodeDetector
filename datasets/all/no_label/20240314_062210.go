
package main

import (
	"fmt"
)

func matrixMultiply(A [][]int, B [][]int) ([][]int, error) {
	m := len(A)
	n := len(A[0])
	p := len(B[0])

	if len(B) != n {
		return nil, fmt.Errorf("incompatible dimensions")
	}

	C := make([][]int, m)
	for i := range C {
		C[i] = make([]int, p)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < p; j++ {
			for k := 0; k < n; k++ {
				C[i][j] += A[i][k] * B[k][j]
			}
		}
	}

	return C, nil
}

func main() {
	A := [][]int{{1, 2}, {3, 4}}
	B := [][]int{{2, 0}, {1, 2}}

	result, err := matrixMultiply(A, B)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	for _, row := range result {
		fmt.Println(row)
	}
}
