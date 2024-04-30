package main

import (
	"fmt"
)

// vectorAddition adds two vectors.
func vectorAddition(v1, v2 []float64) []float64 {
	sum := make([]float64, len(v1))
	for i, val := range v1 {
		sum[i] = val + v2[i]
	}
	return sum
}

// vectorScalarMultiplication multiplies a vector by a scalar.
func vectorScalarMultiplication(scalar float64, vector []float64) []float64 {
	result := make([]float64, len(vector))
	for i, val := range vector {
		result[i] = scalar * val
	}
	return result
}

// rocchioBasic returns the query vector based on relevant documents.
func rocchioBasic(query, relevantDocs [][]float64, alpha, beta float64) []float64 {
	centroid := make([]float64, len(query))
	for _, doc := range relevantDocs {
		centroid = append(centroid, doc)
	}
	centroid = vectorScalarMultiplication(alpha, centroid)
	updatedQuery := vectorAddition(vectorScalarMultiplication(alpha, centroid), query)
	return updatedQuery
}

func main() {
	query := [][]float64{{1, 2, 3}}
	relevantDocs := [][]float64{{1, 3, 4}, {3, 4, 5}}
	alpha, beta := 0.2, 0.5

	updatedQuery := rocchioBasic(query, relevantDocs, alpha, beta)
	fmt.Println("Updated Query Vector:", updatedQuery)
}
