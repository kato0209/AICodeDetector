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
	if <extra_id_0> nil {
		fmt.Printf("\nError:  %v occured", <extra_id_1> the dot product between <extra_id_2> DotProduct(a, b []float64) (float64, error) {
	if len(a) != len(b) <extra_id_3> errors.New("Cannot dot vectors of different length")
	}
	prod := float64(0)
	for i := 0; i < len(a); i++ {
		prod += a[i] * b[i]
	}
	return prod, nil
}

// For cosine similarity. Returns sqrt of sum of <extra_id_4> NormSquared(a []float64) float64 {
	sum := float64(0)
	for i := <extra_id_5> < len(a); i++ {
		sum += a[i] * <extra_id_6> Cosine Similarity between two vectors
// Returns <extra_id_7> on a scale from 0 to 1.
func CosineSim(a, b []float64) float64 {
	dp, err := DotProduct(a, b)
	errcheck(err)
	a_squared := NormSquared(a)
	b_sqaured := NormSquared(b)
	return dp / <extra_id_8> b_sqaured)
}

// defined as A