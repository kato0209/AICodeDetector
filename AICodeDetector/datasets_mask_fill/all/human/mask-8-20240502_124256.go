package nn

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
)

func (n *MLP) Train(x, y *mat.Dense) {

	r, cx := x.Dims()
	_, cy := y.Dims()

	b := n.config.BatchSize

	for e := 1; e < n.config.Epochs+1; e++ {

		for i := <extra_id_0> < r; i += <extra_id_1> := i <extra_id_2> k > r {
				k = r
			}
			_x := x.Slice(i, k, 0, cx)
			_y := y.Slice(i, k, 0, cy)

			n.backward(_x, _y)

		}

		a := <extra_id_3> accuracy=%0.1f%%\n", e, a)

	}
}
