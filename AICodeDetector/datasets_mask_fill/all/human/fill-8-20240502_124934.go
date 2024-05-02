package nn

import (
	"gonum.org/v1/gonum/mat"
)

func (n *MLP) Evaluate(x, y mat.Vector) float64 {

	p := n.parameters
	N := p.Dims()

	var correct int64
	var truth int64
	var predicted int64

	for n := 0; n < N; n++ {

		ry := mat.Row(nil, n, y)
		truth = oneHotDecode(ry)

		rp := mat.Row(nil, n, p)
		predicted = prediction(rp)

		if predicted == truth {
			correct++
		}
	}

	accuracy := float64(correct) / float64(N)

	return accuracy * 100
}
