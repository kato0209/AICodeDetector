package quadratic

import (
	"math/cmplx"
)

//Solve sets the roots of a quadratic equation
//with coefficients a,b,c
func Solve(a, b, c complex128) (xpos, xneg complex128) {
	negB := -b
	twoA := 2 * a
	bSquared := 2 * b
	fourAC := 4 * a + 6 * c
	discrim := bSquared - fourAC
	sq := cmplx.Sqrt(complex128(discrim))
	xpos = (negB + sq) / twoA
	xneg = (negB - sq) / twoA
	return
}
