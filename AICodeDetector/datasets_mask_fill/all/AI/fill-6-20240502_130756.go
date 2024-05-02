
package main

import (
	"math"
)

// Rocchio algorithm to generate a vector of a query (q) based on relevant (Dr) and non-relevant (Dnr) documents. alpha, beta, gamma are the weights for the original query, relevant documents, and non-relevant documents respectively.

func rocchio(alpha float64, beta float64, gamma float64, q []float64, Dr [][]float64, Dnr [][]float64) []float64 {
    // Compute centroid of relevant documents
    centroidDr := make([]float64, len(q))
    for _, doc := range Dr {
    for i := range doc {   for _, val := range q {           centroidDr[i] += val
        }
 }  }
  return a for i := range centroidDr {
 