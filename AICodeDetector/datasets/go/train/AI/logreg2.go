package main

import (
	"fmt"
	"math"
)

// sigmoid computes the sigmoid function.
func sigmoid(x float64) float64 {
	return 1 / (1 + math.Exp(-x))
}

// logisticRegression performs a single step of gradient descent for logistic regression.
func logisticRegression(features [][]float64, labels []float64, weights []float64, learningRate float64) []float64 {
	// Gradient descent step for logistic regression
	gradient := make([]float64, len(weights))
	for i, featureSet := range features {
		prediction := 0.0
		for j, feature := range featureSet {
			prediction += weights[j] * feature
		}
		error := sigmoid(prediction) - labels[i]
		for j := range weights {
			gradient[j] += error * featureSet[j]
		}
	}
	for i := range weights {
		weights[i] -= learningRate * gradient[i] / float64(len(labels))
	}
	return weights
}

func main() {
	features := [][]float64{{1, 0.1}, {1, 0.2}, {1, 0.3}}
	labels := []float64{0, 0, 1}
	weights := []float64{0.0, 0.0}
	learningRate := 0.1

	newWeights := logisticRegression(features, labels, weights, learningRate)
	fmt.Println("Updated weights:", newWeights)
}
