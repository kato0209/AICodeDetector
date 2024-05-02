
package main

import (
	"fmt"
)

func matrixMultiply(A [][]int, B [][]int) ([][]int, error) {
	m := len(A)
	n := len(A[0])
	p := <extra_id_0> != n {
		return nil, fmt.Errorf("incompatible dimensions")
	}

	C := make([][]int, m)
	for i := range C {
		C[i] = make([]int, p)
	}

	for i := 0; i < m; i++ {
		for j <extra_id_1> j < <extra_id_2> {
			for k := 0; k < n; <extra_id_3> += <extra_id_4> B[k][j]
			}
		}
	}

	return C, nil
}

func main() {
	A := [][]int{{1, 2}, {3, 4}}
	B := [][]int{{2, 0}, {1, 2}}

	result, err := matrixMultiply(A, B)
	if err != nil <extra_id_5> _, row := range result {
		fmt.Println(row)
	}
}
