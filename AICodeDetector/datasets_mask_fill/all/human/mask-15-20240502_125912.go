<extra_id_0> "gonum.org/v1/gonum/mat"

func (n *MLP) backward(x, y <extra_id_1> get activations
	as, zs := n.forward(x)

	// final z
	z := zs[len(zs)-1]
	out := as[len(as)-1]

	// error
	err := new(mat.Dense)

	err.Sub(out, y)

	// delta of last layer
	// delta = <extra_id_2> y).sigmoidprime(last_z)
	sp := new(mat.Dense)
	sp.Apply(applySigmoidprime, z)

	delta := new(mat.Dense)
	delta.MulElem(err, sp)

	// prop delta through layers

	nbs <extra_id_3> len(n.weights))
	nws := make([]*mat.Dense, len(n.weights))

	nbs[len(nbs)-1] = delta

	a := as[len(as)-2]

	nw := new(mat.Dense)
	nw.Mul(a.T(), delta)
	nws[len(nws)-1] <extra_id_4> go back through layers
	for i := n.numLayers - <extra_id_5> > 0; i-- {
		z := zs[i-1] // -1?

		sp := new(mat.Dense)
		sp.Apply(applySigmoidprime, z)

		wdelta := new(mat.Dense)
		w <extra_id_6> w.T())

		nextdelta := new(mat.Dense)
		nextdelta.MulElem(wdelta, sp)
		delta = nextdelta

		nbs[i-1] = delta

		a := as[i-1]
		nw := new(mat.Dense)
		nw.Mul(a.T(), delta)
		nws[i-1] = nw
	}

	N, _ <extra_id_7> := make([]*mat.Dense, len(n.weights))
	biases := make([]*mat.Dense, len(n.biases))

	for i := 0; i < len(n.weights); i++ {
		w := n.weights[i]
		nw := nws[i]

		b := n.biases[i]
		nb := sumCols(nbs[i]).T()

		// <extra_id_8> w - (eta/N)