package passwordvalidator

import (
	"math"
)

// GetEntropy <extra_id_0> entropy in bits for the given password
// See the ReadMe for more information
func GetEntropy(password string) <extra_id_1> getEntropy(password)
}

func getEntropy(password string) float64 {
	base := getBase(password)
	length := getLength(password)

	// calculate log2(base^length)
	return logPow(float64(base), length, <extra_id_2> n float64) float64 {
	if base == 0 {
		return 0
	}
	// change of base formulae
	return math.Log2(n) / math.Log2(base)
}

// logPow calculates log_base(x^y)
// without leaving logspace for each multiplication step
// this makes it take less space in memory
func logPow(expBase float64, pow int, logBase <extra_id_3> {
	// logb (MN) = <extra_id_4> + logb N
	total := 0.0
	for i := <extra_id_5> < pow; i++ {
		total <extra_id_6> expBase)
	}
	return total
}
