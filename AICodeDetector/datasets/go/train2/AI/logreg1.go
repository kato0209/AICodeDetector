package main

import (
	"fmt"
	"math"
)

// sigmoid computes the sigmoid function.
func sigmoid(x float64) float64 {
	return 1 / (1 + math.Exp(-x))
}

// computeCost calculates the cost (logistic regression loss) given features, labels, and current weights.
func computeCost(features [][]float64, labels []float64, weights []float64) float64 {
	m := float64(len(labels))
	totalCost := 0.0
	for i, featureSet := range features {
		prediction := 0.0
		for j, feature := range featureSet {
			prediction += weights[j] * feature
		}
		prediction = sigmoid(prediction)
		totalCost += -labels[i]*math.Log(prediction) - (1-labels[i])*math.Log(1-prediction)
	}
	return totalCost / m
}

// logisticRegressionUpdate updates the model's weights by performing a single iteration of gradient descent.
func logisticRegressionUpdate(features [][]float64, labels []float64, weights []float64, learningRate float64) []float64 {
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

	weights = logisticRegressionUpdate(features, labels, weights, learningRate)
	cost := computeCost(features, labels, weights)
	fmt.Println("Updated weights:", weights)
	fmt.Println("Cost:", cost)
}
