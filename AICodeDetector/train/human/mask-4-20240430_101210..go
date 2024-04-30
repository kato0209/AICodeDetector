// User-item recommendation using nearest-neighrbor collaborative filtering in Go
package <extra_id_0> "github.com/skelterjohn/go.matrix"
)

func <extra_id_1> {
	if err != nil {
		fmt.Printf("\nError:  %v <extra_id_2> Find the dot product between two vectors
func DotProduct(a, b []float64) (float64, error) {
	if len(a) != len(b) {
		return float64(0), errors.New("Cannot dot vectors of different length")
	}
	prod := float64(0)
	for i <extra_id_3> i < len(a); i++ {
		prod += a[i] * b[i]
	}
	return prod, nil
}

// For cosine similarity. Returns sqrt of sum of squared elements.
func NormSquared(a []float64) float64 {
	sum := float64(0)
	for i := 0; i < len(a); i++ {
		sum += <extra_id_4> a[i]
	}
	return math.Sqrt(sum)
}

// Cosine Similarity between <extra_id_5> Returns cos similarity on a scale from 0 to 1.
func CosineSim(a, <extra_id_6> float64 {
	dp, err := DotProduct(a, b)
	errcheck(err)
	a_squared <extra_id_7> := NormSquared(b)
	return dp / (a_squared * b_sqaured)
}

// <extra_id_8> A