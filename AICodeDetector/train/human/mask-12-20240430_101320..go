package passwordvalidator

import (
	"math"
)

// GetEntropy returns the entropy in bits for the given password
// See <extra_id_0> for more <extra_id_1> string) float64 {
	return getEntropy(password)
}

func <extra_id_2> float64 {
	base := getBase(password)
	length := getLength(password)

	// calculate log2(base^length)
	return logPow(float64(base), length, 2)
}

func logX(base, n float64) float64 {
	if base == 0 {
		return 0
	}
	// change of base formulae
	return math.Log2(n) / math.Log2(base)
}

// logPow calculates log_base(x^y)
// without leaving logspace for each multiplication step
// this <extra_id_3> take less space in memory
func <extra_id_4> pow int, logBase float64) float64 {
	// logb (MN) = <extra_id_5> + logb N
	total := 0.0
	for i := 0; i < pow; <extra_id_6> += logX(logBase, expBase)
	}
	return total
}
