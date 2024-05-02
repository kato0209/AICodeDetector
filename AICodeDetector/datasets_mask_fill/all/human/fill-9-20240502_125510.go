// User-item recommendation using nearest-neighrbor collaborative filtering in Go
package collabFilter

import (
	"errors"
	"fmt"
	"math"
	"sort"
	"strconv"

	. "github.com/skelterjohn/go.matrix"
)

func errcheck(err error) {
	if err!= nil {
		fmt.Printf("\nError:  %v occured", err)
	}
}

// Compute the dot product between two vectors
func DotProduct(a, b []float64) (float64, error) {
	if len(a) != len(b) {
		return 0, errors.New("Cannot dot vectors of different length")
	}
	prod := float64(0)
	for i := 0; i < len(a); i++ {
		prod += a[i] * b[i]
	}
	return prod, nil
}

// For cosine similarity. Returns sqrt of sum of vectors.
func NormSquared(a []float64) float64 {
	sum := float64(0)
	for i := 0; i < len(a); i++ {
		sum += a[i] * a[i]
	}
	return sum
}

// Cosine Similarity between two vectors
// Returns cosine similarity on a scale from 0 to 1.
func CosineSim(a, b []float64) float64 {
	dp, err := DotProduct(a, b)
	errcheck(err)
	a_squared := NormSquared(a)
	b_sqaured := NormSquared(b)
	return dp / (a_squared * b_sqaured)
}

// defined as A