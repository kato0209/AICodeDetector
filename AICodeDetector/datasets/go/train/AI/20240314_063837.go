
package main

import (
	"fmt"
	"math"
)

// logisticFunction calculates the logistic function
func logisticFunction(x float64) float64 {
	return 1 / (1 + math.Exp(-x))
}

// logisticRegression predicts the probability that a given data point belongs to a certain class
func logisticRegression(features []float64, weights []float64, bias float64) float64 {
	z := bias
	for i := range features {
		z += features[i] * weights[i]
	}
	return logisticFunction(z)
}

func main() {
	features := []float64{1.0, 2.0, 3.0} // Example features
	weights := []float64{0.2, -0.1, 0.4} // Example weights
	bias := 0.1                          // Example bias

	// Predict the probability
	probability := logisticRegression(features, weights, bias)
	fmt.Println(probability) // Output the predicted probability
}
