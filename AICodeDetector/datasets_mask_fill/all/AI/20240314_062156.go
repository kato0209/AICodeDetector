
package main

import (
	"fmt"
	"math"

	"gonum.org/v1/gonum/mat"
)

// sigmoid function applies the sigmoid function on a float64
func sigmoid(x float64) float64 {
	return 1.0 / (1.0 + math.Exp(-x))
}

// logisticRegression function performs the logistic regression on the dataset
// X is the feature matrix with rows as the training examples and columns as features
// y is the target vector
// alpha is the learning rate
// iterations is the number of iterations for gradient descent
func logisticRegression(X *mat.Dense, y *mat.VecDense, alpha float64, iterations int) *mat.VecDense {
	// Number of training examples and features
	m, n := X.Dims()

	// Initialize weights (theta) with zeros
	theta := mat.NewVecDense(n, nil)

	for i := 0; i < iterations; i++ {
		// Compute hypothesis (predictions) using sigmoid function
		var predictions mat.VecDense
		predictions.MulVec(X, theta)
		predictions.Apply(func(i int, v float64) float64 { return sigmoid(v) }, &predictions)

		// Compute the error
		var error mat.VecDense
		error.SubVec(&predictions, y)

		// Compute gradient
		var gradient mat.Dense
		gradient.Mul(X.T(), &error)
		gradient.Scale(alpha/float64(m), &gradient)

		// Update theta (weights)
		theta.SubVec(theta, gradient.ColView(0))
	}

	return theta
}

func main() {
	// Example usage
	// Define features X (with a column of ones for the intercept) and target y
	X := mat.NewDense(3, 2, []float64{
		1.0, 0.0,
		1.0, 1.0,
		1.0, 2.0,
	})
	y := mat.NewVecDense(3, []float64{0, 0, 1})

	// Learning rate and iterations
	alpha := 0.1
	iterations := 1000

	// Perform logistic regression
	theta := logisticRegression(X, y, alpha, iterations)

	fmt.Println("Theta:", theta.RawVector().Data)
}
