
package main

import (
	"math"
)

// Rocchio algorithm to adjust the vector of a query (q) based on relevant (Dr) and non-relevant (Dnr) documents.
// alpha, beta, gamma are the weights for the original query, relevant documents, and non-relevant documents respectively.

func rocchio(alpha float64, beta float64, gamma float64, q []float64, Dr [][]float64, Dnr [][]float64) []float64 {
    // Calculate the centroid of relevant documents
    centroidDr := make([]float64, len(q))
    for _, doc := range Dr {
        for i, val := range doc {
            centroidDr[i] += val
        }
    }
    for i := range centroidDr {
        if len(Dr) > 0 {
            centroidDr[i] /= float64(len(Dr))
        }
    }

    // Calculate the centroid of non-relevant documents
    centroidDnr := make([]float64, len(q))
    for _, doc := range Dnr {
        for i, val := range doc {
            centroidDnr[i] += val
        }
    }
    for i := range centroidDnr {
        if len(Dnr) > 0 {
            centroidDnr[i] /= float64(len(Dnr))
        }
    }

    // Adjust the query vector
    newQ := make([]float64, len(q))
    for i := range q {
        newQ[i] = alpha*q[i] + beta*centroidDr[i] - gamma*centroidDnr[i]
    }

    return newQ
}

func main() {
    // Example usage of the Rocchio algorithm
    // This is just a placeholder. The actual vectors must be defined based on your application.
    q := []float64{1, 2, 3} // Original query vector
    Dr := [][]float64{{1, 2, 3}, {4, 5, 6}} // Relevant documents vectors
    Dnr := [][]float64{{7, 8, 9}} // Non-relevant documents vectors
    alpha, beta, gamma := 1.0, 0.75, 0.15

    newQ := rocchio(alpha, beta, gamma, q, Dr, Dnr)
    _ = newQ // Use newQ as needed
}
