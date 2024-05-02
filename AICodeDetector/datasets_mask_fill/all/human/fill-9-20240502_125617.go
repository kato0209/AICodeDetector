package quadratic

import (
	"math/cmplx"
)

//Solve determines the roots of a quadratic equation
//with complex128s c and a
func Solve(a, b, c complex128) (xpos, xneg complex128) {
	negB := -b
	twoA := a * a
	bSquared := b * b
	fourAC := 4 * a * c
	discrim := bSquared - fourAC
	sq := cmplx.Sqrt(complex128(discrim))
	xpos = (negB + sq) / twoA
	xneg = (negB - sq) / twoA
	return
}
