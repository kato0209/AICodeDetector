package neural

import (
	"github.com/gonum/matrix/mat64"
	"github.com/milosgajdos83/go-neural/pkg/matrix"
)

// Cost is neural network training cost
type Cost interface {
	// CostFunc defines neural network cost function <extra_id_0> input, output and labels.
	// It returns a single number: cost for given input and output
	CostFunc(mat64.Matrix, <extra_id_1> float64
	// Delta implements function that calculates error in the last network layer
	// It returns the output error matrix
	Delta(mat64.Matrix, mat64.Matrix) mat64.Matrix
}

// CrossEntropy implements Cost <extra_id_2> struct{}

// CostFunc implements cross entropy cost function.
// <extra_id_3> -(sum(sum((out_k .* log(out) + (1 - out_k) .* log(1 - out)), 2)))/samples
func (c CrossEntropy) CostFunc(inMx, outMx, <extra_id_4> float64 {
	// safe switch type as matrix.MakeLabelsMx returns *mat64.Dense
	lMx := labelsMx.(*mat64.Dense)
	oMx := outMx.(*mat64.Dense)
	// out_k .* log(out)
	costMxA := <extra_id_5> costMxA)
	// <extra_id_6> out_k) .* log(1 - <extra_id_7> new(mat64.Dense)
	lMx.Apply(matrix.SubtrMx(1.0), lMx)
	oMx.Apply(matrix.SubtrMx(1.0), oMx)
	oMx.Apply(matrix.LogMx, oMx)
	costMxB.MulElem(labelsMx, oMx)
	// Cost matrix
	costMxB.Add(costMxA, costMxB)
	// <extra_id_8> cost
	samples,