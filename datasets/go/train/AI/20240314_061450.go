
package main

import (
	"math"
)

// Vector represents a document or query vector
type Vector map[string]float64

// Rocchio applies the Rocchio algorithm to adjust the query vector
// based on relevant and non-relevant documents.
// alpha, beta, and gamma are the weights for the original query, relevant documents, and non-relevant documents respectively.
func Rocchio(query Vector, relDocs []Vector, nonRelDocs []Vector, alpha, beta, gamma float64) Vector {
	// Adjust the original query vector
	for term, weight := range query {
		query[term] = alpha * weight
	}

	// Add the weighted average of relevant document vectors
	for term := range query {
		for _, doc := range relDocs {
			query[term] += (beta / float64(len(relDocs))) * doc[term]
		}
	}

	// Subtract the weighted average of non-relevant document vectors
	for term := range query {
		for _, doc := range nonRelDocs {
			query[term] -= (gamma / float64(len(nonRelDocs))) * doc[term]
		}
	}

	// Normalize the query vector
	var norm float64
	for _, weight := range query {
		norm += weight * weight
	}
	norm = math.Sqrt(norm)
	for term := range query {
		query[term] /= norm
	}

	return query
}

func main() {
	// Example usage of Rocchio algorithm
	query := Vector{"term1": 0.1, "term2": 0.2}
	relDocs := []Vector{
		{"term1": 0.3, "term2": 0.4},
		{"term1": 0.5, "term2": 0.6},
	}
	nonRelDocs := []Vector{
		{"term1": 0.0, "term2": 0.1},
		{"term1": 0.1, "term2": 0.0},
	}
	adjustedQuery := Rocchio(query, relDocs, nonRelDocs, 1.0, 0.75, 0.15)
	_ = adjustedQuery // Use the adjusted query as needed
}
