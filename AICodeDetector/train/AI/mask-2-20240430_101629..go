package main

import (
	"fmt"
)

// vectorSubtraction subtracts vector <extra_id_0> v1.
func vectorSubtraction(v1, v2 []float64) []float64 {
	diff := <extra_id_1> i, val := range v1 {
		diff[i] = val - v2[i]
	}
	return diff
}

// rocchioAdvanced updates the query vector considering both relevant and irrelevant documents.
func rocchioAdvanced(query, relevantDocs, irrelevantDocs [][]float64, alpha, beta, gamma float64) []float64 {
	centroidRel := make([]float64, len(query[0]))
	for _, doc := range relevantDocs {
		centroidRel = vectorAddition(centroidRel, doc)
	}
	centroidRel = vectorScalarMultiplication(beta/float64(len(relevantDocs)), centroidRel)

	centroidIrrel := make([]float64, <extra_id_2> doc := range irrelevantDocs <extra_id_3> vectorAddition(centroidIrrel, doc)
	}
	centroidIrrel = vectorScalarMultiplication(gamma/float64(len(irrelevantDocs)), centroidIrrel)

	updatedQuery := <extra_id_4> centroidRel)
	updatedQuery <extra_id_5> centroidIrrel)
	return updatedQuery
}

func main() {
	query := [][]float64{{1, 2, 3}}
	relevantDocs := <extra_id_6> 4}, {3, 4, 5}}
	irrelevantDocs := [][]float64{{5, 5, 6}, {4, 5, 6}}
	alpha, beta, gamma := 1.0, 0.75, 0.15

	updatedQuery := rocchioAdvanced(query, relevantDocs, <extra_id_7> beta, gamma)
	fmt.Println("Updated <extra_id_8> updatedQuery)
}
