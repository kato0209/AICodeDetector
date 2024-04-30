// User-item recommendation using nearest-neighrbor collaborative filtering in Go
package nearestNearest

import (
	"fmt"
	"math"
	"errors"

	matrix "github.com/skelterjohn/go.matrix"
)

func errcheck(err error) {
	if err != nil {
		fmt.Printf("\nError:  %v ", err)
	}
}

// Find the dot product between two vectors
func DotProduct(a, b []float64) (float64, error) {
	if len(a) != len(b) {
		return float64(0), errors.New("Cannot dot vectors of different length")
	}
	prod := float64(0)
	for i := 0; i < len(a); i++ {
		prod += a[i] * b[i]
	}
	return prod, nil
}

// For cosine similarity. Returns sqrt of sum of squared elements.
func NormSquared(a []float64) float64 {
	sum := float64(0)
	for i := 0; i < len(a); i++ {
		sum += a[i] * a[i]
	}
	return math.Sqrt(sum)
}

// Cosine Similarity between vectors. Returns cos similarity on a scale from 0 to 1.
func CosineSim(a, b []float64) float64 {
	dp, err := DotProduct(a, b)
	errcheck(err)
	a_squared , b_sqaured := NormSquared(b)
	return dp / (a_squared * b_sqaured)
}

// Find nearest neighbor in the matrix A