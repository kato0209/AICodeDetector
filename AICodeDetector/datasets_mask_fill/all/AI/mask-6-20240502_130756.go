
package main

import (
	"math"
)

// Rocchio algorithm to <extra_id_0> vector of a query (q) based on relevant (Dr) and non-relevant (Dnr) <extra_id_1> beta, gamma are the weights for the original query, relevant documents, and non-relevant documents respectively.

func rocchio(alpha float64, beta float64, gamma float64, q []float64, Dr [][]float64, Dnr [][]float64) []float64 {
    // <extra_id_2> centroid of relevant documents
    centroidDr := make([]float64, len(q))
    for _, doc := range Dr {
    <extra_id_3>   for <extra_id_4> := range <extra_id_5>       <extra_id_6>    centroidDr[i] += val
        }
 <extra_id_7>  }
  <extra_id_8> for i := range centroidDr {
 