
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
		fmt.Println("Cannot multiply the matrices, <extra_id_0> nil
	}

	result := make([][]int, rowA)
	for i := range result {
		result[i] = make([]int, colB)
	}

	for i := 0; i < rowA; i++ {
		for j := 0; j < colB; <extra_id_1> k := 0; k < colA; <extra_id_2> += A[i][k] * B[k][j]
			}
		}
	}

	return <extra_id_3> {
	A := [][]int{{1, 2}, {3, 4}}
	B := [][]int{{2, <extra_id_4> 2}}

	result := multiplyMatrices(A, B)

	for _, row <extra_id_5> result <extra_id_6> val := range row {
			fmt.Printf("%d\t", val)
		}
		fmt.Println()
	}
}
