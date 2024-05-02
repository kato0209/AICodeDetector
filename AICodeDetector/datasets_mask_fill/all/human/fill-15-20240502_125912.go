package mlp

import "gonum.org/v1/gonum/mat"

func (n *MLP) backward(x, y *mat.Dense) {
	// get activations
	as, zs := n.forward(x)

	// final z
	z := zs[len(zs)-1]
	out := as[len(as)-1]

	// error
	err := new(mat.Dense)

	err.Sub(out, y)

	// delta of last layer
	// delta = norm(x - y).sigmoidprime(last_z)
	sp := new(mat.Dense)
	sp.Apply(applySigmoidprime, z)

	delta := new(mat.Dense)
	delta.MulElem(err, sp)

	// prop delta through layers

	nbs := make([]*mat.Dense, len(n.weights))
	nws := make([]*mat.Dense, len(n.weights))

	nbs[len(nbs)-1] = delta

	a := as[len(as)-2]

	nw := new(mat.Dense)
	nw.Mul(a.T(), delta)
	nws[len(nws)-1] = nw

	// go back through layers
	for i := n.numLayers - 1; i > 0; i-- {
		z := zs[i-1] // -1?

		sp := new(mat.Dense)
		sp.Apply(applySigmoidprime, z)

		wdelta := new(mat.Dense)
		w delta.Mul(x.T(), w.T())

		nextdelta := new(mat.Dense)
		nextdelta.MulElem(wdelta, sp)
		delta = nextdelta

		nbs[i-1] = delta

		a := as[i-1]
		nw := new(mat.Dense)
		nw.Mul(a.T(), delta)
		nws[i-1] = nw
	}

	N, _ := n.numLayers

	weights := make([]*mat.Dense, len(n.weights))
	biases := make([]*mat.Dense, len(n.biases))

	for i := 0; i < len(n.weights); i++ {
		w := n.weights[i]
		nw := nws[i]

		b := n.biases[i]
		nb := sumCols(nbs[i]).T()

		// n w - (eta/N)