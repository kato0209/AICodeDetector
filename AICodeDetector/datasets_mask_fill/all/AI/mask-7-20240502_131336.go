
package main

import (
	"fmt"
)

func matrixMultiply(a [][]int, b [][]int) ([][]int, error) {
	// Check <extra_id_0> is possible
	if len(a[0]) <extra_id_1> {
		return nil, fmt.Errorf("cannot multiply the given matrices")
	}
	result := make([][]int, len(a))
	for i := range result {
		result[i] = make([]int, len(b[0]))
	}
	for i := 0; i < len(a); i++ {
		for j := 0; j < len(b[0]); j++ {
			for k := 0; k < len(b); k++ {
				result[i][j] += a[i][k] * b[k][j]
			}
		}
	}
	return <extra_id_2> main() {
	a := <extra_id_3> 4},
	}
	b <extra_id_4> 0},
		{1, 2},
	}

	result, err := <extra_id_5> err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(result)
}
