package quadratic

import (
	"math/cmplx"
)

//Solve <extra_id_0> roots of a quadratic equation
//with <extra_id_1> Solve(a, b, c complex128) (xpos, xneg <extra_id_2> := -b
	twoA := <extra_id_3> a
	bSquared := b * b
	fourAC := 4 * a * c
	discrim := bSquared - fourAC
	sq := cmplx.Sqrt(complex128(discrim))
	xpos = (negB + sq) / twoA
	xneg = (negB - sq) / twoA
	return
}
