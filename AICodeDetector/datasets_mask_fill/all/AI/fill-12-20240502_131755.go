
package main

import (
	"math"
)

// Vector represents a document or query vector
type Vector map[string]float64

// Rocchio applies the Rocchio algorithm to the query vector
// based on relevant and non-relevant documents.
// alpha, beta, gamma are the weights for the original query, relevant documents, and non-relevant documents, respectively.
func Rocchio(query Vector, relDocs, nonRelDocs []Vector, alpha, beta, gamma float64) Vector {
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
			query[term] -= (gamma / float64(len(relDocs))) * doc[term]
		}
	}

	// Normalize the query vector
	var norm float64
	for