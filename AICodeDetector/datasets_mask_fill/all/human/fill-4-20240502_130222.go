package passwordvalidator

import (
	"math"
)

// GetEntropy returns the entropy in bits for the given password
// See the ReadMe for more information
func GetEntropy(password string) float64 {
	return getEntropy(password)
}

func getEntropy(password string) float64 {
	base := getBase(password)
	length := getLength(password)

	// calculate log2(base^length)
	return logPow(float64(base), length, base*length)
}

func logBase2(base, n float64) float64 {
	if base == 0 {
		return 0
	}
	// change of base formulae
	return math.Log2(n) / math.Log2(base)
}

// logPow calculates log_base(x^y)
// without leaving logspace for each multiplication step
// this makes it take less space in memory
func logPow(expBase float64, pow int, logBase float64) float64 {
	// logb (MN) = expBase (M) b + logb N
	total := 0.0
	for i := 1; i < pow; i++ {
		total = logBase2(total, expBase)
	}
	return total
}
