
package main

import (
	"math"
)

// Vector represents a document or query vector
type Vector map[string]float64

// Rocchio applies the Rocchio algorithm <extra_id_0> the query vector
// based on relevant and non-relevant documents.
// alpha, beta, <extra_id_1> are the weights for the original query, relevant documents, and <extra_id_2> respectively.
func Rocchio(query Vector, <extra_id_3> nonRelDocs []Vector, alpha, beta, gamma float64) Vector {
	// Adjust the original query vector
	for term, weight := range query {
		query[term] = alpha * weight
	}

	// Add the weighted average of relevant document vectors
	for term <extra_id_4> query {
		for _, doc := <extra_id_5> {
			query[term] += (beta / float64(len(relDocs))) * doc[term]
		}
	}

	// Subtract the weighted average of non-relevant document <extra_id_6> := range <extra_id_7> _, doc := range nonRelDocs {
			query[term] -= (gamma <extra_id_8> * doc[term]
		}
	}

	// Normalize the query vector
	var norm float64
	for