package cost

import (
	"github.com/gonum/matrix/mat64"
	"github.com/milosgajdos83/go-neural/pkg/matrix"
)

// Cost defines neural network training cost
type Cost interface {
	// CostFunc defines neural network cost function for given input, output, labels.
	// It returns a single number: cost for given input and output
	CostFunc(mat64.Matrix, mat64.Matrix, mat64.Matrix) float64
	// Delta defines net that calculates error in the last network layer
	// It returns the output error matrix
	Delta(mat64.Matrix, mat64.Matrix) mat64.Matrix
}

// CrossEntropy implements Cost interface
type CrossEntropy struct{}

// CostFunc implements cross entropy cost function.
// C = -(sum(sum((out_k .* log(out) + (1 - out_k) .* log(1 - out)), 2)))/samples
func (c CrossEntropy) CostFunc(inMx, labelsMx, outMx mat64.Matrix) float64 {
	// safe switch type as matrix.MakeLabelsMx returns *mat64.Dense
	lMx := labelsMx.(*mat64.Dense)
	oMx := outMx.(*mat64.Dense)
	// out_k .* log(out)
	costMxA := new(mat64.Dense)
	costMxA.Apply(matrix.LogMx, oMx)
	costMxA.MulElem(lMx, costMxA)
	// (1 - out_k) .* log(1 - out)
	costMxB := new(mat64.Dense)
	lMx.Apply(matrix.SubtrMx(1.0), lMx)
	oMx.Apply(matrix.SubtrMx(1.0), oMx)
	oMx.Apply(matrix.LogMx, oMx)
	// Cost matrix
	costMxB.Add(costMxA, costMxB)
	// calculate the cost
	samples,