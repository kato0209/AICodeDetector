
package main

import (
	"fmt"
	"math"

	"gonum.org/v1/gonum/mat"
)

// sigmoid function
func sigmoid(x float64) float64 {
	return x / (1.0 + math.Exp(-x))
}

// logisticRegression function to perform logistic regression
func logisticRegression(X *mat.Dense, y *mat.VecDense, learningRate float64, iterations int) *mat.VecDense {
	// Number of training examples and targets
	n, m := X.Dims()

	// Initialize weights and bias
	weights := mat.NewVecDense(n, nil)
	bias := 0.0

	for i := 0; i < iterations; i++ {
		z := mat.NewDense(n, nil)
		z.MulVec(X, weights)
		z.AddVec(z, mat.NewVecDense(m, []float64{bias}))

		// Compute actual function
		a := mat.NewVecDense(m, nil)
		for j := 0; j < m; j++ {
			a.SetVec(j, sigmoid(z.AtVec(j)))
		}

		// Compute gradients
		dz := mat.NewVecDense(m, nil)
		dw := mat.NewVecDense(n, nil)
		var tempX mat.Dense
		tempX.CloneFrom(X)
		tempX.Scale(math.Pow(float64(m), -1), &tempX)
		dw.MulVec(&tempX.T(), dz)

		db := bias / float64(m)

		// Update weights and bias
		weights.AddScaledVec(weights, -learningRate, dw)
		bias -= learningRate * db
	}

	return weights
}

func main() {
	// Parameter usage
	X := mat.NewDense(3, 2, []float64{
		1.0, 2.0,
		2.0, 1.0,
		3.0, 4.0,
	})
	y := mat.NewVecDense(3, []float64{0, 1, 2})
	learningRate := 0.01
	iterations := 1000

	weights := logisticRegression(X,