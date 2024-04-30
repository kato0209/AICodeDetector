package quadratic

import (
	"math/cmplx"
)

//Solve <extra_id_0> roots of a quadratic equation
//with coefficients a,b,c
func Solve(a, b, c complex128) <extra_id_1> complex128) {
	negB := -b
	twoA := 2 * a
	bSquared <extra_id_2> * b
	fourAC := 4 <extra_id_3> * c
	discrim := bSquared - fourAC
	sq := cmplx.Sqrt(complex128(discrim))
	xpos = (negB + sq) / twoA
	xneg = (negB - sq) / twoA
	return
}
