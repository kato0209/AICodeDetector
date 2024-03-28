
package main

import (
    "fmt"
    "math"
)

// Vector represents a document vector in the vector space model.
type Vector map[string]float64

// Add adds one vector to another.
func (v Vector) Add(other Vector) Vector {
    result := make(Vector)
    for term, value := range v {
        result[term] = value
    }
    for term, value := range other {
        result[term] += value
    }
    return result
}

// Multiply multiplies each term in the vector by a scalar.
func (v Vector) Multiply(scalar float64) Vector {
    result := make(Vector)
    for term, value := range v {
        result[term] = value * scalar
    }
    return result
}

// Rocchio calculates the updated query vector based on the Rocchio algorithm.
func Rocchio(originalQuery Vector, relevantDocs []Vector, irrelevantDocs []Vector, alpha, beta, gamma float64) Vector {
    // Represents the sum of relevant documents vectors
    sumRelevant := make(Vector)
    for _, docVec := range relevantDocs {
        sumRelevant = sumRelevant.Add(docVec)
    }

    // Represents the sum of irrelevant documents vectors
    sumIrrelevant := make(Vector)
    for _, docVec := range irrelevantDocs {
        sumIrrelevant = sumIrrelevant.Add(docVec)
    }

    // Calculate the new query vector
    newQuery := originalQuery.Multiply(alpha)
    if len(relevantDocs) > 0 {
        newQuery = newQuery.Add(sumRelevant.Multiply(beta / float64(len(relevantDocs))))
    }
    if len(irrelevantDocs) > 0 {
        newQuery = newQuery.Add(sumIrrelevant.Multiply(-gamma / float64(len(irrelevantDocs))))
    }

    return newQuery
}

func main() {
    // Example usage of Rocchio algorithm
    originalQuery := Vector{"information": 1, "retrieval": 1}
    relevantDocs := []Vector{
        {"information": 2, "retrieval": 3},
        {"information": 1, "retrieval": 2, "relevant": 1},
    }
    irrelevantDocs := []Vector{
        {"information": 1, "retrieval": 1, "irrelevant": 2},
    }
    alpha, beta, gamma := 1.0, 0.75, 0.15

    newQuery := Rocchio(originalQuery, relevantDocs, irrelevantDocs, alpha, beta, gamma)
    fmt.Println("Updated Query Vector:", newQuery)
}
