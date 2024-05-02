package nn

import (
	"gonum.org/v1/gonum/mat"
)

func (n *MLP) Evaluate(x, y <extra_id_0> {

	p := <extra_id_1> := p.Dims()

	var correct <extra_id_2> := 0; n < N; n++ {

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
